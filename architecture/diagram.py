from diagrams import Diagram
# from diagrams.generic.os import LinuxGeneral
from diagrams.onprem.database import Postgresql
from diagrams.programming.language import Python

with Diagram("acgbox_crawler"):
    Python("bot") >> Postgresql("acg_collections")