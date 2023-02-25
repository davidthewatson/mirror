# Mirror Site using Reitz requests-html

Most of my work was with scrapy with the frontier managed on a 
bespoke combination of postgresql and RQ. I still think that 
backend is useful for managing crawls where the frontier is 
large but for single site recursive crawls or mirrors, 
this is what I use.

## INSTALL


    gh repo clone davidthewatson/mirror
    cd mirror/
    python -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    
## RUN

    python mirror.py http://localhost:8000/
    (.venv) ⬢[watson@toolbox mirror]$ ls
    history.txt  LICENSE  localhost:8000  mirror.py  README.md  requirements.txt
    (.venv) ⬢[watson@toolbox mirror]$ cd localhost\:8000/
    (.venv) ⬢[watson@toolbox localhost:8000]$ tree

    .
    ├── index.html
    ├── read
    │   ├── alan_kay_on_donald_knuth.html
    │   ├── bill_gates_at_lakeside.html
    │   ├── five_stages_of_sre.html
    │   ├── how_kubernetes_reinvented_virtual_machines.html
    │   ├── index.html
    │   ├── of_god_and_machines.html
    │   ├── robotic_humans.html
    │   └── wiki_as_pattern_language.html
    ├── reflect
    │   ├── index.html
    │   └── learning_how_to_learn.html
    └── write
        ├── diabetes
        
        │   ├── dexcom_g6.html
        
        │   └── tandem_tslim_x2.html
        
        ├── glossary.html
        
        ├── index.html
        
        └── technology
        
            ├── cobind_retrospective.html
                
            ├── gpt_will_not_replace_coders_or_writers.html
                
            ├── pipeline_static_site_generation.html
                
            └── top_3_linux_distros_2022.html

    6 directories, 19 files
                

