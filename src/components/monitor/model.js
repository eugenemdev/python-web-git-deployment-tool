import Service from '../../services/services.js';

/**
 * Model for component Home
 * @returns list of posts
 */

class Model{
    constructor(){                 
        
    }

    async getState(){
        let state = await new Service().getState();                        
        return state;
    }

}

export default Model;