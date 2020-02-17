'use strict';
import Model from './model.js';
import View from './view.js';

/**
 * controller Monitor
 * @param model
 * @param view
 * 
 * @return state
 */

class Monitor {
    constructor(){
        this.model = new Model();
        this.view = new View();                
    }
            
    async render(){        
        let state = await this.model.getState();                
        let section =  await this.view.appendState(state);
        return section                        
    }

    after_render(){
    }

}

export default Monitor;