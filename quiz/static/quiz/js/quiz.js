document.addEventListener('DOMContentLoaded', () => {
    const search_btn = document.getElementById('searchbtn');
    api_url = '/api/categoriescategories/?format=api'
    async function get_categories(){
        await fetch(api_url)
        .then(res => res.text())
       .then(data =>{
        console.log(data);
       })
        
    }

    search_btn.addEventListener('click', (e) => {
        e.preventDefault();
        const search_input = document.getElementById('input'); // Get the input element
        console.log("The input value is " + search_input.value); // Log the input value
        search_input.value = ''; // Clear the input field
        console.log(get_categories());
    });
});
