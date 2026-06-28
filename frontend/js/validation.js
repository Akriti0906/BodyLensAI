function validateInputs(data) {

    if (!data.age || data.age <= 0) {
        alert("Please enter a valid age.");
        return false;
    }

    if (!data.gender) {
        alert("Please select your gender.");
        return false;
    }

    if (!data.height_cm || data.height_cm <= 0) {
        alert("Please enter a valid height.");
        return false;
    }

    if (!data.weight_kg || data.weight_kg <= 0) {
        alert("Please enter a valid weight.");
        return false;
    }

    if (!data.activity_level) {
        alert("Please select activity level.");
        return false;
    }

    if (!data.goal) {
        alert("Please select your goal.");
        return false;
    }

    if (!data.condition) {
        alert("Please select your condition.");
        return false;
    }

    return true;

}