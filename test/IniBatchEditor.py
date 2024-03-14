import os, json
import configparser


class CustomConfigParser(configparser.ConfigParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 保持区分大小写
        self.optionxform = str

    def write(self, fp, space_around_delimiters=False):
        """Write an .ini-format representation of the configuration state."""
        if space_around_delimiters:
            d = " {} ".format(self._delimiters[0])
        else:
            d = self._delimiters[0]
        if self._defaults:
            self._write_section(fp, self.default_section, self._defaults.items(), d)
        for section in self._sections:
            self._write_section(fp, section, self._sections[section].items(), d)

    def _write_section(self, fp, section_name, section_items, delimiter):
        """Write a single section to the specified `fp`."""
        fp.write("[{}]\n".format(section_name))
        for key, value in section_items:
            fp.write("{}{}{}\n".format(key, delimiter, value))
        fp.write("\n")


def main():
    with open('config.json', 'r', encoding='utf-8') as file:
        configs = json.load(file)

    for config in configs:
        parser = CustomConfigParser(strict=False)

        for path in config['paths']:
            parser.read(path, encoding='utf-8')

            modifications = []

            for update in config['updates']:
                section, key, value = update['section'], update['key'], update['value']

                if parser.has_section(section) and parser.has_option(section, key):
                    original_value = parser.get(section, key)
                    parser.set(section, key, value)
                    modifications.append(f"{section}.{key}: {original_value} -> {value}")

            if modifications:
                with open(path, 'w', encoding='utf-8') as configfile:
                    # 写入文件时不在等号周围添加空格
                    parser.write(configfile, space_around_delimiters=False)
                print(f"Updated {path} with the following changes:")
                for modification in modifications:
                    print(f"    {modification}")


if __name__ == '__main__':
    print("For any questions or concerns, please contact:")
    print("Pengcheng.yan@cowellchina.com")
    print("=========================================")
    try:
        main()
    except Exception as e:
        print(str(e))

    os.system("pause")
