employees=[{"name":"john","id":102,"country":"usa"}]
departments=[{"name":"IT","id":12,"hod":{"name":"mr.Bewon","id":11,}},{"name":"CS","id":11,"hod":{"name":"mr.Holding","id":10,}}]
print("printing employee data....")
for emp in employees:
    print(f"name:{emp['name']},id:{emp['id']},country:{emp['country']}")
print("\nprinting departments..")
for i,dept in enumerate(departments,start=1):
    print(f"department{i}:")
    print(f"name:{dept['name']},id:{dept['id']}")
print("\n hod details..")
for dept in departments:
    hod=dept['hod']
    print(f"{dept['name']} hod name:{hod['name']},id:{hod['id']}")