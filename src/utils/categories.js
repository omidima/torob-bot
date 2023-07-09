
function extract_categories() {
    /**
     * getting products categories from torob site
     * 
     * # how to run: open the https://torob.com/ and paste this script in console then rnu extract_categories() and get json string data.
     * @return string : a string type of json
     */
    let a = document.querySelectorAll(".dropitems")
    let items = []
    a.forEach((l) => { l.querySelectorAll(".columnelement").forEach((i) => { i.querySelectorAll("a").forEach((b) => { items.push({ name: b.innerHTML, link: b.href }) }) }) })
    let standard_data = items.map((item) => { return { name: item.name.replace("<span>", "").replace("</span>", ""), link: item.link.split("/")[4] } })
    return standard_data;
}