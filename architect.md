# Description
Quick point form explination of why we chose what we chose. 

# Block Diagram

```mermaid
block-beta
    columns 3
    F[/"Front End"\]:3
    ext["Chrome Extension"]:3
        v["vite"] 
        space
        react["React"]
    
    space down1<[" "]>(updown) space
    

    B[\"Back End"/]:3
    g["Gallium-A40-Cluster"]:3
    s["server.py"]
    ti["Tensor-Image"]:2
    space:3

    space:2 presentation 
    space:3
    cache["cache.py] space aml["accessMl.py"]
    space:3 
    db[("SQLite")]:2 space
    cache --> db
    s --> cache
    cache --> s
    s --> aml
    aml --> presentation
    presentation --> s


  

    TI{{"Tensor-Image Docker"}}:3
       
       ic["imageCaptioning.py"]
       htmlp["htmlparser.py"]
       dh["dockerHelper.py"]
       space kwf["keywordfinder.py"] space
       dh --> aml
    style ic fill:#2B66D4
    style TI fill:#2B66D4
    style dh fill:#2B66D4
    style htmlp fill:#2B66D4
    style kwf fill:#2B66D4
    style ti fill:#2B66D4

    style F fill:#A700AF,stroke:#fa96ff, text_color:"#FFFF"
    style ext fill:#A700AF,stroke:#fa96ff, text_color:"#FFFF"
    style v fill:#A700AF,stroke:#fa96ff, text_color:"#FFFF"
    style react fill:#A700AF,stroke:#fa96ff, text_color:"#FFFF"
```
