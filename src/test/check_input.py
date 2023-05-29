import re

entrada = re.search(r"\d+", input())
dia = int(entrada.group(0)) if entrada is not None else None