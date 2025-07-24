import os
import ast
import tree_sitter_java as tsjava
import tree_sitter_cpp as tscpp
from tree_sitter import Language, Parser

# Modern tree-sitter API - no need to build library
JAVA = Language(tsjava.language())
CPP = Language(tscpp.language())
parser = Parser()

def extract_python_functions(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        source_code = f.read()

    tree = ast.parse(source_code)
    results = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_code = ast.get_source_segment(source_code, node)
            docstring = ast.get_docstring(node) or ""
            results.append({
                "function_name": node.name,
                "docstring": docstring,
                "code": func_code,
                "file_path": file_path,
                "language": "python"
            })
    return results

def extract_with_tree_sitter(file_path, lang_obj, language_name):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    # Handle both old and new tree-sitter API
    try:
        parser.set_language(lang_obj)  # Old API
    except AttributeError:
        parser.language = lang_obj     # New API
    
    tree = parser.parse(bytes(code, "utf8"))
    root_node = tree.root_node

    results = []
    
    def traverse_node(node):
        # Different node types for different languages
        function_types = {
            "java": ["method_declaration", "constructor_declaration"],
            "cpp": ["function_definition", "function_declarator"]
        }
        
        if node.type in function_types.get(language_name, []):
            func_code = code[node.start_byte:node.end_byte]
            
            # Try to find function name
            func_name = "unknown"
            if language_name == "java":
                # Look for identifier in method declaration
                for child in node.children:
                    if child.type == "identifier":
                        func_name = code[child.start_byte:child.end_byte]
                        break
            elif language_name == "cpp":
                # For C++, look for function_declarator or identifier
                for child in node.children:
                    if child.type == "function_declarator":
                        for subchild in child.children:
                            if subchild.type == "identifier":
                                func_name = code[subchild.start_byte:subchild.end_byte]
                                break
                        break
                    elif child.type == "identifier":
                        func_name = code[child.start_byte:child.end_byte]
                        break
            
            results.append({
                "function_name": func_name,
                "docstring": "",  # Can be enhanced to extract comments
                "code": func_code,
                "file_path": file_path,
                "language": language_name
            })
        
        # Recursively traverse children
        for child in node.children:
            traverse_node(child)
    
    traverse_node(root_node)
    return results

def extract_all_code():
    all_data = []
    
    # Get the script's directory and go up one level to find data directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)  # Go up one level from backend
    data_dir = os.path.join(project_root, "data")
    
    base_dirs = {
        "python": (os.path.join(data_dir, "python"), extract_python_functions),
        "java": (os.path.join(data_dir, "java"), lambda path: extract_with_tree_sitter(path, JAVA, "java")),
        "cpp": (os.path.join(data_dir, "cpp"), lambda path: extract_with_tree_sitter(path, CPP, "cpp")),
    }

    for lang, (dir_path, extractor) in base_dirs.items():
        if not os.path.exists(dir_path):
            print(f"⚠️  Directory {dir_path} not found, skipping {lang}")
            continue
            
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith((".py", ".java", ".cpp", ".cc", ".cxx")):
                    full_path = os.path.join(root, file)
                    try:
                        result = extractor(full_path)
                        all_data.extend(result)
                        print(f"✅ Processed {full_path}: {len(result)} functions")
                    except Exception as e:
                        print(f"❌ Failed on {full_path}: {e}")
    return all_data

if __name__ == "__main__":
    extracted = extract_all_code()
    print(f"\n🎉 Extracted {len(extracted)} functions total")
    
    if extracted:
        print("\n📋 Sample output:")
        for e in extracted[:3]:  # sample output
            print("▶️", e["function_name"], "|", e["language"])
            print(e["code"][:200] + "..." if len(e["code"]) > 200 else e["code"])
            print("="*40)
    else:
        print("No functions found. Make sure your data directories exist and contain code files.")