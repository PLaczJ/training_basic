from shutil import copytree

from django.shortcuts import render
from django.template.loader import render_to_string

from config.settings.base import BASE_DIR
from django.template import Context, Template

from django.template.backends.dummy import TemplateStrings

TEMPLATE_APP = BASE_DIR / "demo"


class Mytemplate(TemplateStrings):

    def __init__(self, params):
        super().__init__(params)
        self.debug = ""
        self.template_libraries = ""
        self.template_builtins = ""



def generate_apps():
    app_numbers = 5
    for id in range(app_numbers):
        app_name = f"app{id}"
        app_dir = BASE_DIR / app_name
        copytree(TEMPLATE_APP, app_dir)
        view_path = app_dir / "views.py"
        url_include_str = f"{app_name}/, include({app_name}.urls)"

        print(f"'{app_name}'")
        print(url_include_str)
        print("\n")

        params = {"OPTIONS": {},
                  "NAME": {"DUMMY"},
                  "DIRS": [],
                  "APP_DIRS": False
                  }

        with open(view_path, "r+") as f:
            template = Template("".join(f.readlines()), engine=Mytemplate(params))
            rendered_html = template.render({"Model": "ModelDemo"})
            f.write(rendered_html)



if __name__ == "__main__":
    generate_apps()
