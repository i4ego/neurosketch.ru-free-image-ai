import requests
import base64, json

print("FREE neurosketch.ru IMAGE AI")
print("this proj using free neurosketch.ru api")
print("if you want to generate images at website, use https://techtravel.neurosketch.ru/styles")
print("by i4ego\n")

style = input("Style (ghibli, malevich, vangogh, picasso, lego, banksy): >>> ")
input_file = input("Input file (name, .jpg/.jpeg file, eg. \"\"): >>> ")

with open(input_file, "rb") as f:
    file = f.read()

print("Generating...")
p = requests.post("https://techtravel.neurosketch.ru/api/ai/generate", {"sketch":f"data:image/jpeg;base64,{base64.b64encode(file).decode()}", "style":style}, stream=True, headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36", "Referer" : "https://techtravel.neurosketch.ru/draw"}, verify=False)
print("Generated!")
with open("response.json", "w") as f:
    f.write(p.text)
try:
    ph = json.loads(p.text)
    if "error" in ph:
        print("Unknown error.")
        raise SystemExit
except TypeError as err:
    print(f"json: {p.text}\n\n")
    print(err)
    raise SystemExit

print(f"json: {p.text}\n\n")
print(f"URL: {ph["url"]}")