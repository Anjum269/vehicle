from vehicle import vehicle_details
def test_vehicle_details():
    expected_output = (
        Vehicle Number : "KA25P3808"
        Owner_Name : "Anjum"
        Vehicle_type : "Car"
        Year_of_Manufacture : "2025"
    )
    assert vehicle_details("KA25P3808","Anjum", "Car" , "2025") == expected_output
