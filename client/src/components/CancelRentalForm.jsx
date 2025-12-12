import { useState, useEffect } from "react";
import axios from "axios";

export default function CancelRentalForm() {
  const [rentalId, setRentalId] = useState("");
  const [rentals, setRentals] = useState([]);


  useEffect(() => {
    axios
      .get("http://localhost:8000/rentals/active")
      .then((res) => setRentals(res.data))
      .catch((err) => console.error(err));
  }, []);

  const cancelRental = async () => {
    if (!rentalId) {
      alert("Please select a rental to cancel");
      return;
    }

    try {
      await axios.delete(`http://localhost:8000/rentals/${rentalId}`); 
      alert("Rental cancelled successfully!");
      
      setRentals(rentals.filter((r) => r.id !== Number(rentalId)));
      setRentalId("");
    } catch (err) {
      alert(err.response?.data?.detail || "Error cancelling rental");
    }
  };

  return (
    <div className="space-y-3">
      <select
        value={rentalId}
        onChange={(e) => setRentalId(e.target.value)}
        className="w-full border p-2 rounded"
      >
        <option value="">Select an active rental</option>
        {rentals.map((r) => (
          <option key={r.id} value={r.id}>
            Rental #{r.id} - Car ID: {r.car_id} ({r.user_name})
          </option>
        ))}
      </select>

      <button
        onClick={cancelRental}
        className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700"
      >
        Cancel Rental
      </button>
    </div>
  );
}
