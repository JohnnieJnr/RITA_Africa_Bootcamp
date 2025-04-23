employee = ["Mark","John","Jennifer","Rita","Anita"]
departments = ["Sales", "HR","IT","Finance","Marketing"]
ratings = [4.5, 3.8, 5.0, 2.5, 4.0]
eligible_department = ("Sales", "IT", "Marketing")
min_rating = 4.0

for i in range (len(employee)):
    name = employee[i]
    department = departments[i]
    rating = ratings[i]

    if department in eligible_department and rating >= min_rating:
        print(f"{name} from {department} is eligible for the bonus")
    else:
        print(f"{name} from {department} is not eligible for the bonus")