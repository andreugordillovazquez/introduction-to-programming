# Exercise 1

print("BREAKDOWN OF BILLS AND COINS")
d = int(input("Insert here the amount in euros (€): "))

#Loop that keeps the program running until the user enters an amount less than zero.
while d > 0:
  a1 = d//500
  a2 = d % 500
  b1 = a2 // 200
  b2 = a2 % 200
  c1 = b2 // 100
  c2 = b2 % 100
  d1 = c2 // 50
  d2 = c2 % 50
  e1 = d2 // 20
  e2 = d2 % 20
  f1 = e2 // 10
  f2 = e2 % 10
  g1 = f2 // 5
  g2 = f2 % 5
  h1 = g2 // 2
  h2 = g2 % 2
  i1 = h2 // 1

  if a1 != 0:
    if a1 == 0:
      print("We have 1 500€ bill.")
    if a1 > 0:
      print("We have", a1, "500€ bills.")

  if a2 != 0:
    if b1 == 1:
      print("We have 1 200€ bill.")
    if b1 > 1:
      print("We have", b1, "200€ bills.")

  if b2 != 0:
    if c1 == 1:
      print("We have 1 100€ bill.")
    if c1 > 1:
      print("We have", c1, "100€ bills.")

  if c2 != 0:
    if d1 == 1:
      print("We have 1 50€ bill.")
    if d1 > 1:
      print("We have", d1, "50€ bills.")

  if d2 != 0:
    if e1 == 1:
      print("We have 1 20€ bill.")
    if e1 > 1:
      print("We have", e1, "20€ bills.")

  if e2 != 0:
    if f1 == 1:
      print("We have 1 10€ bill.")
    if f1 > 1:
      print("We have", f1, "10€ bills.")

  if f2 != 0:
    if g1 == 1:
      print("We have 1 5€ bill.")
    if g1 > 1:
      print("We have", g1, "5€ bills.")

  if g2 != 0:
    if h1 == 1:
      print("We have 1 2€ coin.")
    if h1 > 1:
      print("We have", h1, "2€ coins.")

  if h2 != 0:
    if i1 == 1:
      print("We have 1 1€ coin.")
    if i1 > 1:
      print("We have", i1, "1€ coins.")

  d = int(input("Insert here the amount in euros (€): "))
