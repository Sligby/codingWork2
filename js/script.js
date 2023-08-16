   

    async function favNumFact(){
        let res = await axios.get ("http://numbersapi.com/11?json")
        console.log(res)
};

document.getElementById('get-fact').addEventListener('click', async () => {
    const favoriteNumber = 11; 
    const url = `http://numbersapi.com/${favoriteNumber}?json=true`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        const factText = data.text;

        document.getElementById('fact-text').textContent = factText;
    } catch (error) {
        console.error('An error occurred:', error);
    }
});
