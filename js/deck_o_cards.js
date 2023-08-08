const drawButton = document.getElementById('draw-button');
const cardContainer = document.getElementById('card-container');

let deckId;
let remainingCards = 0;

function createNewDeck() {
    return fetch('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
        .then(response => response.json())
        .then(data => {
            deckId = data.deck_id;
            remainingCards = data.remaining;
        });
}

function drawCard() {
    if (remainingCards === 0) {
        cardContainer.innerHTML = '<p>No cards left in the deck.</p>';
        drawButton.disabled = true;
        return;
    }

    return fetch(`https://deckofcardsapi.com/api/deck/${deckId}/draw/?count=1`)
        .then(response => response.json())
        .then(data => {
            const card = data.cards[0];
            const cardText = document.createElement('p');
            cardText.textContent = `${card.value} of ${card.suit}`;
            cardContainer.appendChild(cardText);
            remainingCards = data.remaining;
        });
}

drawButton.addEventListener('click', () => {
    drawCard();
});

// On page load, create a new deck and enable the draw button
createNewDeck().then(() => {
    drawButton.disabled = false;
});
