
build/my-languages.so: \
    language/tree-sitter-typescript \
    language/tree-sitter-python
	./tools/bin/python build/build_languages.py


language/tree-sitter-python:
	git clone https://github.com/tree-sitter/tree-sitter-python


language/tree-sitter-typescript:
	git clone https://github.com/tree-sitter/tree-sitter-typescript

