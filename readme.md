# Markdown merger

This is a simple tool to merge multiple markdown files into one.

## Usage

By default, the tool will output to `output.md` and will look for files in the `files` directory.

```bash
python merge.py -file-path <path to file> -output <output file>
```

### Include notation

To include a file, use the following notation:

```markdown
![$include-md](path/to/file.md)
```
