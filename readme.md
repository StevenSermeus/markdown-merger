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

## Limitations

- The tool will not do import recusion, so you can't include a file that includes another file.

- The tool will not update the links in the files, so if you include a image, it will not be displayed in the output file. So you have to setup the links in the files to point to the correct location after the merge.

## Todo

- [ ] Add support for images paths update
