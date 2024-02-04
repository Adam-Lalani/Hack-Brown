const server = 'http://localhost:8080';

export async function fetchURL(input) {
    const serverUrl = `${server}/?input=${input}`;

    try {
        const response = await fetch(serverUrl);
        if (!response.ok) {
            console.log("ERROR")
            throw new Error('Failed to get response from backend');
        }

        // Invoke response.json() to get the parsed JSON data
        const responseData = await response.json();

        console.log(responseData); // Log or use the parsed JSON data
        return responseData;
    } catch (error) {
        console.log("ERROR2")
        console.error('Error:', error);
        throw error;
    }
}
