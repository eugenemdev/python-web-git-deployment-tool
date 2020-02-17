class Service {
    constructor(){
        this.options = { method: 'GET', headers: {'Content-Type': 'application/json'}};                        
    }
    
    async getState(){
        const options = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        };
        try {            
            const response = await fetch('/getstate', options)
            const json = await response.json();
            console.log(json)
            return json
        } catch (err) {
            console.log('Error getting documents', err)
        }
    }
}

export default Service;