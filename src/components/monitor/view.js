'use strict';

/**
 * View for component Monitor 
 * @param monitoring state
 * @returns html view for home page
 */

class View {
    constructor(){           
    }   

    appendState(state){
                
        let view =  /*html*/`
            <section class="section">
                <h3> Python Web Deployment Monitoring Tool</h3>
                <ul>
                    <li>Current System : ${state.system.name}</li>
                    <li>Last Reboot : ${state.system.lastreboot}</li>
                </ul>
                <p>Repository : ${String.raw`${state.repo.name}`}</p>
                <ul>
                    <li>Last pull :  ${state.repo.date}</li>
                    <li>Current status : ${state.repo.status}</li>                    
                    <li>Previous commit : ${state.repo.previous_commit}</li>
                    <li>Last commit :  ${state.repo.last_commit}</li>
                    <li>Info: ${state.repo.description}</li>
                </ul>
                <p>Build</p>
                <ul>
                    <li>Last buid :  ${state.build.date}</li>
                    <li>Current status :  ${state.build.status}</li>
                    <li>Info: ${state.build.description}</li>
                </ul>
                <p>Deploy</p>
                <ul>
                    <li>Last deploy : ${state.deploy.date}</li>
                    <li>Current status : ${state.deploy.status}</li>
                    <li>Info: ${state.deploy.description}</li>
                </ul>
            </section>`
    return view;        
    }
}

export default View;