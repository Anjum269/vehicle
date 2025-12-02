def vehicle_details(number, owner_name, vehicle_type,year_of_manufacture):
    result=(
        f"Vehicle Number: {number}\n"
        f" Owner Name: { owner_name}\n"
        f" Vehicle Type: {vehicle_type}\n"
        f"Year of Manufature: {year_of_manufacture}\n"
    )
    return result
if __name__=="__main__":
  number = "KA25P3808   
  owner_name = "Anjum"
  vehicle_type = "Car"
  year_of_manufacture = "2025"
    print(vehicle_details( number,owner_name,vehicle_type,year_of_manufacture))
