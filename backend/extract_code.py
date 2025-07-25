import os
import ast
import javalang
import re

def extract_python_functions(file_path):
    results = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_code = ast.get_source_segment(source, node)
                docstring = ast.get_docstring(node) or ""
                results.append({
                    "function_name": node.name,
                    "docstring": docstring,
                    "code": func_code,
                    "file_path": file_path,
                    "language": "python"
                })
    except Exception as e:
        print(f"[Python Parse Error] {file_path}: {e}")
    return results

def extract_java_functions(file_path):
    results = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
        tree = javalang.parse.parse(source)
        for _, node in tree.filter(javalang.tree.MethodDeclaration):
            method_name = node.name
            docstring = node.documentation if hasattr(node, 'documentation') and node.documentation else ""
            results.append({
                "function_name": method_name,
                "docstring": docstring,
                "code": "",  # Optionally use regex if needed
                "file_path": file_path,
                "language": "java"
            })
    except Exception as e:
        print(f"[Java Parse Error] {file_path}: {e}")
    return results

def extract_cpp_functions(file_path):
    results = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()

        # Very naive function pattern (doesn't cover all edge cases)
        function_pattern = re.compile(
            r'(?:[\w:<>\*&\s]+)\s+(\w+)\s*\(([^)]*)\)\s*{',
            re.MULTILINE
        )
        for match in function_pattern.finditer(source):
            func_name = match.group(1)
            func_signature = match.group(0)
            results.append({
                "function_name": func_name,
                "docstring": "",
                "code": func_signature + "  // Body not captured",
                "file_path": file_path,
                "language": "cpp"
            })

    except Exception as e:
        print(f"[C++ Parse Error] {file_path}: {e}")
    return results

def extract_all_functions(base_path):
    results = []
    for dirpath, _, filenames in os.walk(base_path):
        for file in filenames:
            full_path = os.path.join(dirpath, file)
            if file.endswith(".py"):
                results.extend(extract_python_functions(full_path))
            elif file.endswith(".java"):
                results.extend(extract_java_functions(full_path))
            elif file.endswith(('.cpp', '.cc', '.h', '.hpp')):
                results.extend(extract_cpp_functions(full_path))
    return results

if __name__ == "__main__":
    base_dir = r"C:\Users\FASI OWAIZ AHMED\Desktop\Code_gen\Data"
    all_results = extract_all_functions(base_dir)

    for r in all_results[:5]:
        print("📂", r["language"].upper(), "▶️", r["function_name"])
        print(r["docstring"])
        print("-" * 40)
