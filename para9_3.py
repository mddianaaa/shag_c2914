import  requests

res_pars_list = []
res = requests.get("https://coinmarketcap.com/")
res_text = res.text
parse = res_text.split("<span>")
for pars_elem1 in parse:
    if pars_elem1.startswith("$"):
        for pars_elem2 in pars_elem1.split("</span>"):
            if pars_elem2.startswith("$") and pars_elem2[1].isdigit():
                res_pars_list.append(pars_elem2)

bitcoin = res_pars_list[0]
dogecoin = res_pars_list[7]

print(bitcoin, dogecoin)
