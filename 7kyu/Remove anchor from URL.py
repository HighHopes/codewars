"""Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
# returns 'www.codewars.com'
remove_url_anchor('www.codewars.com#about')

# returns 'www.codewars.com?page=1'
remove_url_anchor('www.codewars.com?page=1') """

def remove_url_anchor(url):
    return url.split("#")[0]

print(remove_url_anchor("www.codewars.com#about"))
print(remove_url_anchor("www.codewars.com/katas/?page=1#about"))
