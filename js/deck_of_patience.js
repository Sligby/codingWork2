let deckId;
let remainingCards = 0;
const drawButton = document.getElementById('draw-butt');
const cardContainer = document.getElementById('card-container');


const deck = {
    async init() {
        let res = await axios.get('https://deckofcardsapi.com/api/deck/new/')
        this.deckId= res.data.deck_id;
    },
    async shuffle() {
        let res = await axios.get(`https://deckofcardsapi.com/api/deck/${this.deckId}/shuffle/`)
        console.log(res)
    },
    async drawCard() {
        try {
            const res = await axios.get(`https://deckofcardsapi.com/api/deck/${this.deckId}/draw/?count=1`);
            console.log('Response from drawCard:', res);
            return res; // Return the response
        } catch (error) {
            console.error('An error occurred in drawCard:', error);
            throw error; // Rethrow the error
        }
    }
    }


window.onload = async () => {
    // Initialize the deck object
    await deck.init();
    console.log('Deck initialized with ID:', deck.deckId)
};


document.getElementById('draw-butt').addEventListener('click', async () => {
    try {
        // Make sure the deck is initialized before drawing a card
        if (!deck.deckId) {
            await deck.init();
        }

        // Draw a card
        const response = await deck.drawCard();

        // Check if the response status is OK
        if (response.status === 200) {
            // Parse the response data as JSON
            const data = await response.data;
            
            // Check if the response data has cards
            if (data.cards && data.cards.length > 0) {
                const card = data.cards[0];
                const cardText = document.createElement('p');
                cardText.textContent = `${card.value} of ${card.suit}`;
                cardContainer.appendChild(cardText);
                remainingCards = data.remaining;
            } else {
                console.error('No cards in the response data.');
            }
        } else {
            console.error('Non-OK response status:', response.status);
        }
    } catch (error) {
        console.error('An error occurred:', error);
    }
});