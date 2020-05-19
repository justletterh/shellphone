function thing(x)
print("...\nyou entered '+"..x.."'\n...")
if x=="1" then
print("which is the country code for the united states\n...")
print("which has the format '+1(xxx)xxx-xxxx'\n...")
elseif x=="44" then
print("which is the country code for the united kingdom\n...")
print("which has many formats\n...")
elseif x=="52" then
print("which is the country code for mexico\n...")
print("which has the format '+52 xxx xxxxxxx'or '+52 xx xxxxxxxx'\n...")
else
print("that country code is not supported\n...")
end
end
function init()
print("...\ntype a country code:")
x=io.read()
x=x:gsub("+","")
return x
end
function main()
return thing(init())
end
main()