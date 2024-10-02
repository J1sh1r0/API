const responses = {
    security: "",
    cost: "",
    learningCurve: "",
    performance: "",
    scalability: "",
    multiplatform: "",
    support: ""
};

let currentStep = 1;

function addMessage(message, sender) {
    const chatContainer = document.getElementById('chat-container');
    const newMessage = document.createElement('div');
    newMessage.classList.add('chat-message', sender);
    newMessage.innerText = message;
    chatContainer.appendChild(newMessage);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function askQuestion(step) {
    switch(step) {
        case 1:
            addMessage("¡Hola! Estoy aquí para ayudarte a seleccionar la mejor base de datos para tus necesidades. ¿Qué nivel de seguridad necesitas para tu base de datos? (Alta/Media/Baja)", "chatbot");
            break;
        case 2:
            addMessage("¿Cuál es tu presupuesto para la implementación de la base de datos? (Bajo/Medio/Alto)", "chatbot");
            break;
        case 3:
            addMessage("¿Qué tan fácil o difícil te gustaría que sea aprender a manejar la base de datos? (Fácil/Moderada/Compleja)", "chatbot");
            break;
        case 4:
            addMessage("¿Cuál es el nivel de rendimiento que esperas para tu base de datos? (Muy alto/Alto/Bueno)", "chatbot");
            break;
        case 5:
            addMessage("¿Qué nivel de escalabilidad necesitas? (Alta/Moderada/Baja)", "chatbot");
            break;
        case 6:
            addMessage("¿Necesitas que la base de datos sea compatible con múltiples plataformas? (Sí/No)", "chatbot");
            break;
        case 7:
            addMessage("¿Qué tipo de soporte prefieres para tu base de datos? (Comunitario/Comercial/Ambos)", "chatbot");
            break;
        case 8:
            evaluateResponses();
            break;
        default:
            addMessage("Gracias por tus respuestas. Si necesitas más ayuda, no dudes en contactarme.", "chatbot");
            break;
    }
}

function handleUserInput() {
    const userInputElement = document.getElementById('user-input');
    const userInput = userInputElement.value.trim().toLowerCase();
    if (userInput === "") return;

    switch(currentStep) {
        case 1:
            responses.security = userInput;
            addMessage(capitalizeFirstLetter(userInput), "user");
            break;
        case 2:
            responses.cost = userInput;
            addMessage(capitalizeFirstLetter(userInput), "user");
            break;
        case 3:
            responses.learningCurve = userInput;
            addMessage(capitalizeFirstLetter(userInput), "user");
            break;
        case 4:
            responses.performance = userInput;
            addMessage(capitalizeFirstLetter(userInput), "user");
            break;
        case 5:
            responses.scalability = userInput;
            addMessage(capitalizeFirstLetter(userInput), "user");
            break;
        case 6:
            responses.multiplatform = userInput;
            addMessage(capitalizeFirstLetter(userInput), "user");
            break;
        case 7:
            responses.support = userInput;
            addMessage(capitalizeFirstLetter(userInput), "user");
            break;
    }

    userInputElement.value = '';
    currentStep++;
    askQuestion(currentStep);
}

function evaluateResponses() {
    let dbChoice = "";

    if (responses.security === "alta" && responses.cost === "alto") {
        dbChoice = "Oracle";
    } else if (responses.security === "media" && responses.cost === "medio") {
        dbChoice = "Microsoft SQL Server";
    } else if (responses.security === "baja" && responses.cost === "bajo") {
        dbChoice = "MySQL";
    } else if (responses.security === "alta" && responses.cost === "bajo") {
        dbChoice = "PostgreSQL";
    } else if (responses.multiplatform === "sí" || responses.multiplatform === "si") {
        dbChoice = "MongoDB";
    } else {
        dbChoice = "PostgreSQL";
    }

    addMessage("Con base en tus respuestas, la base de datos que mejor se adapta a tus necesidades es: " + dbChoice, "chatbot");
    currentStep++;
    askQuestion(currentStep);
}

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

// Función para mostrar el contenido correspondiente
function showContent(section) {
    // Ocultar todas las secciones
    const sections = document.querySelectorAll('.content, .chat-container');
    sections.forEach(sec => sec.style.display = 'none');

    // Mostrar la sección seleccionada
    const selectedSection = document.getElementById(section);
    if (selectedSection) {
        selectedSection.style.display = 'block';
    }
}

// Iniciar el chatbot
askQuestion(currentStep);
