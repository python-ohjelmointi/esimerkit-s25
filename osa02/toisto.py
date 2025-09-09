'''
<select>
<option>1000</option>
<option>2000</option>
<option>3000</option>
<option>4000</option>
</select>
'''

hinta = 0

print("<select>")

while hinta < 10_000:
    hinta = hinta + 1_000
    print(f"  <option>{hinta}</option>")

print("</select>")
