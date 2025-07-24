import os
import ast

def extract_python_functions(file_path):
    results=[]
    for dirpath, _, filename in os.walk(file_path):
        for file in filename:
            full_path = os.path.join(dirpath, file)
            with open(full_path, "r", encoding="utf-8") as f:
                temp_source_code = f.read()
            tree=ast.parse(temp_source_code)
            for i in ast.walk(tree):
                if isinstance(i, ast.FunctionDef):
                    func_code = ast.get_source_segment(temp_source_code, i)
                    docstring = ast.get_docstring(i) or ""
                    results.append({
                        "function_name": i.name,
                        "docstring": docstring,
                        "code": func_code,
                        "file_path": full_path,
                        "language": "python"
                    })
    return results

base_dir = r"C:\Users\FASI OWAIZ AHMED\Desktop\Code_gen\Data\Python"
all_results= extract_python_functions(base_dir)


for r in all_results[:5]:
    print("▶️", r["function_name"])
    # print(r["code"])
    print(r["docstring"])
    print("=" * 40)