#!/usr/bin/env python3

import tomllib
import argparse
from jinja2 import Environment, FileSystemLoader
from typing import Dict
from pathlib import Path


def render_template(template_path: Path, cfg: Dict[str, str]):
    env = Environment(loader=FileSystemLoader(template_path.parent))
    template = env.get_template(template_path.name)
    return template.render(
        **cfg,
    )

def generate_template():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--template-config", type=Path, help="TOML template config"
    )
    parser.add_argument(
        "-t", "--template-path", type=Path, help="Path to the project template"
    )
    parser.add_argument("-o", "--output", type=Path, help="Output file path")
    args = parser.parse_args()
    with open(args.template_config, "rb") as cfg_file:
        cfg = tomllib.load(cfg_file)
        rendered = render_template(args.template_path, cfg)
        with open(args.output, "w", encoding="utf-8") as output_file:
            output_file.write(rendered)


if __name__ == "__main__":
    try:
        generate_template()
    except Exception as err:
        print(f"Failed to generate project template. Error: {err}")
        exit(1)
