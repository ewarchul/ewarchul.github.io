alias g := generate

set positional-arguments

@generate sub:
  python3 generate_template.py -c configs/$1.toml -t templates/msc-project.jinja -o teaching/$1.html
