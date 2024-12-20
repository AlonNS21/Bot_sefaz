// // //chat.js

let userName = '';

// Adiciona evento de tecla para o campo de nome do usuário
document.getElementById("user-name").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        setUserName();
    }
});

// Função para definir o nome do usuário
function setUserName() {
    userName = document.getElementById('user-name').value.trim();
    if (userName === "") {
        alert("Por favor, insira seu nome.");
        return;
    }

    // Atualiza a interface
    document.getElementById('name-container').style.display = 'none';
    document.getElementById('chat-box').style.display = 'block';
    document.getElementById('input-container').style.display = 'flex';

    // Mensagens de boas-vindas
    const mensagens = [
        `E aí ${userName}, beleza, em que posso te ajudar?`,
        `Fala ${userName}, como posso ajudar?`,
        `Oi ${userName}, tudo bem? Em que posso ser útil?`,
        `Olá ${userName}, estou aqui para te ajudar, o que você precisa?`,
        `Hey ${userName}, como posso ser útil hoje?`,
        `Saudações ${userName}, em que posso te auxiliar?`,
        `Olá ${userName}, o que você precisa?`,
        `Hey! ${userName}, Como vai? Vamos espalhar um pouco de magia por aí? Zueira, em que posso ajudar?`,
        `Oi, ${userName}, beleza? Estou aqui para te guiar, o que você precisa?`,
        `${userName}, e aí, meu chapa! Preparado para dominar o domínio? Kkkk, o que vai querer saber hoje?`,
        `Olá! ${userName}, como anda a vida? Estou pronto para te auxiliar hoje!`,
        `${userName} parceiro(a)! Vamos botar pra quebrar? O que vai ser hoje?`,
        `${userName}? E aí, chuchu! Pronto para bater um papo?`,
        `Olá, ${userName}, estou à disposição para te auxiliar!`,
        `${userName}, tudo tranquilo? Estou aqui para te ajudar, firme e forte!`,
        `Ei, ${userName}! Tô aqui para desenrolar qualquer situação!`,
        `Hey, ${userName}, beleza? Estou pronto para te dar uma força!`,
        `Olá, pipoca! Bora resolver essas paradas?`,
        `Oi, pão na chapa! Como posso facilitar o seu dia?`,
        `Olá, ovo frito! Estou à disposição para te auxiliar!`
    ];

    // Seleciona uma mensagem aleatória
    const mensagemAleatoria = mensagens[Math.floor(Math.random() * mensagens.length)];
    addMessageToChatBox("Bot", mensagemAleatoria);
}

// Adiciona evento de tecla para o campo de mensagem
document.getElementById("message").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});

// Função para enviar mensagem
function sendMessage() {
    const message = document.getElementById('message').value.trim();
    if (message === "") return;

    addMessageToChatBox(userName, message);
    document.getElementById('message').value = "";

    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const botResponse = linkify(data.response);
        addMessageToChatBox("Bot", botResponse);
    })
    .catch(error => {
        console.error('Erro:', error);
        addMessageToChatBox("Bot", "Desculpe, houve um erro ao processar sua mensagem.");
    });
}

// Função para adicionar mensagem ao chat
function addMessageToChatBox(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');

    // Define a classe da mensagem com base no remetente
    if (sender === userName) {
        messageElement.classList.add('user-message');
    } else {
        messageElement.classList.add('bot-message');
        
        // Adiciona eventos para mostrar a imagem ao passar o mouse
        messageElement.addEventListener("mouseover", () => {
            document.getElementById("hidden-image").style.display = 'block';
        });
        messageElement.addEventListener("mouseout", () => {
            document.getElementById("hidden-image").style.display = 'none';
        });
    }

    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Rola para a última mensagem
}

// Função para transformar URLs em links clicáveis
function linkify(text) {
    const urlPattern = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig;
    return text.replace(urlPattern, url => `<a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a>`);
}

// Função para expandir a imagem ao clicar
function expandirImagem(img) {
    const modal = document.getElementById('modal');
    const modalImg = document.getElementById('imagem-expandida');
    
    modal.style.display = "block"; // Exibe o modal
    modalImg.src = img.src; // Define a imagem no modal
}

// Função para fechar o modal ao clicar fora da imagem ou no "X"
function fecharModal() {
    const modal = document.getElementById('modal');
    modal.style.display = "none";
}
