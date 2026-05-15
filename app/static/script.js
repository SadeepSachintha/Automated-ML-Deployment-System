const inputs = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width'];
const speciesMap = {
    'setosa': '🌸',
    'versicolor': '🌿',
    'virginica': '🌺',
    'unknown': '❓'
};

const updateValue = (id, val) => {
    document.getElementById(`${id}_val`).textContent = val;
};

const predict = async () => {
    const data = {};
    inputs.forEach(id => {
        data[id] = parseFloat(document.getElementById(id).value);
    });

    const resultDiv = document.getElementById('result');
    const loadingDiv = document.getElementById('loading');

    // Show loading state
    resultDiv.style.opacity = '0.3';
    loadingDiv.classList.remove('hidden');

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById('species_name').textContent = result.species;
            document.getElementById('prediction_id').textContent = result.prediction;
            document.getElementById('species_icon').textContent = speciesMap[result.species] || '🌸';
        } else {
            console.error('Prediction failed:', result.detail);
        }
    } catch (error) {
        console.error('Error:', error);
    } finally {
        resultDiv.style.opacity = '1';
        loadingDiv.classList.add('hidden');
    }
};

// Add listeners to all inputs
inputs.forEach(id => {
    const el = document.getElementById(id);
    el.addEventListener('input', (e) => {
        updateValue(id, e.target.value);
        debouncePredict();
    });
});

// Debounce to avoid too many requests
let timeout;
const debouncePredict = () => {
    clearTimeout(timeout);
    timeout = setTimeout(predict, 300);
};

// Initial prediction
predict();
