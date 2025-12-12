import { useState, useEffect } from "react";
import axios from "axios";

export default function RentCarForm() {
  const [form, setForm] = useState({
    car_id: "",
    user_name: "",
    start_date: "",
    end_date: "",
  });

  const [cars, setCars] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/cars/")
      .then((res) => setCars(res.data))
      .catch((err) => console.error(err));
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const rentCar = async () => {
    if (!form.car_id) {
      alert("Please select a car");
      return;
    }

    try {
      const payload = { 
        user_name: form.user_name,
        start_date: form.start_date,
        end_date: form.end_date,
      };

      const res = await axios.post(
        `http://localhost:8000/rentals/${form.car_id}/rent`,
        payload
      );

      alert("Car rented successfully!");
      console.log(res.data);
    } catch (err) {
      alert(err.response?.data?.detail || "Error renting car");
    }
  };

  return (
    <div className="space-y-3">
      <select
        name="car_id"
        value={form.car_id}
        onChange={handleChange}
        className="w-full border p-2 rounded"
      >
        <option value="">Select a car</option>
        {cars.map((car) => (
          <option key={car.id} value={car.id}>
            {car.make} {car.model} ({car.year}) - ₹{car.daily_rate}/day
          </option>
        ))}
      </select>

      <input
        type="text"
        name="user_name"
        placeholder="Your Name"
        onChange={handleChange}
        className="w-full border p-2 rounded"
      />

      <input
        type="date"
        name="start_date"
        onChange={handleChange}
        className="w-full border p-2 rounded"
      />

      <input
        type="date"
        name="end_date"
        onChange={handleChange}
        className="w-full border p-2 rounded"
      />

      <button
        onClick={rentCar}
        className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
      >
        Rent Car
      </button>
    </div>
  );
}
