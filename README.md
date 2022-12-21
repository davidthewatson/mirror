# Mirror Site using Reitz requests-html

I've been working on web scraping for decades. Most of my work was with scrapy with the frontier managed on a bespoke combination of postgresql and RQ. I still think that backend is useful for managing crawls where the frontier is large but for single page crawls or mirrors, this is what I use.

## INSTALL

TBD

## RUN

    (.venv) watson@asus-zenbook:~/Github/mirror$ python mirror.py https://davidwatson.org/
    (.venv) watson@asus-zenbook:~/Github/mirror$ tree davidwatson.org/
    davidwatson.org/
    ├── index.html
    ├── read
    │   ├── alan_kay_on_donald_knuth.html
    │   ├── bill_gates_at_lakeside.html
    │   ├── five_stages_of_sre.html
    │   ├── how_kubernetes_reinvented_virtual_machines.html
    │   ├── index.html
    │   ├── neil_postman_on_parental_control_of_children_information_environment.html
    │   ├── of_god_and_machines.html
    │   └── wiki_as_pattern_language.html
    ├── reflect
    │   ├── index.html
    │   ├── learning_how_to_learn.html
    └── write
        ├── index.html
        └── technology
            ├── cobind_retrospective.html
            ├── design.html
            ├── gpt_wont_replace_coders_or_writers.html
            ├── pipeline_static_site_generation.html
            └── top_3_linux_distros_2022.html
    5 directories, 17 files
