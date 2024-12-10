document.addEventListener('DOMContentLoaded', () => {
    const search_btn = document.getElementById('searchbtn');
    const api_url = '/api/categories/'; // Correct endpoint

    // Function to fetch categories from the API
    async function get_categories() {
        try {
            const response = await fetch(api_url, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json', // Ensure JSON response
                    'Content-Type': 'application/json'
                }
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json(); // Parse JSON response
            console.log("Fetched categories:", data);
            return data; // Return the data for further processing
        } catch (error) {
            console.error("Error fetching categories:", error);
            alert("Failed to fetch categories. Please try again later.");
            return null;
        }
    }

    // Function to render categories in the DOM
    function renderCategories(categories) {
        const categoriesContainer = document.getElementById('categories-container'); // Assuming this container exists in your HTML
        categoriesContainer.innerHTML = ''; // Clear previous content

        if (categories && categories.length > 0) {
            categories.forEach(category => {
                const categoryElement = document.createElement('div');
                categoryElement.className = 'category-item'; // Add styles as needed
                categoryElement.innerHTML = `
                    <h3>${category.name}</h3>
                    <img src="${category.image}" alt="${category.name}" class="category-image"/>
                    <p>Total Marks: ${category.total_marks}</p>
                `;
                categoriesContainer.appendChild(categoryElement);
            });
        } else {
            categoriesContainer.innerHTML = '<p>No categories found.</p>';
        }
    }

    // Event listener for the search button
    search_btn.addEventListener('click', async (e) => {
        e.preventDefault();
        const search_input = document.getElementById('input');
        console.log("The input value is " + search_input.value); // Log the input value

        // Fetch and render categories
        const categories = await get_categories();
        if (categories) {
            renderCategories(categories);
        }

        search_input.value = ''; // Clear the input field after processing
    });
});
