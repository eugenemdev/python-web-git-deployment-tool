'use strict'
import Model from './model.js'
import View from './view.js'

/**
 * controller Monitor
 * @param model
 * @param view
 * @return state
 */

class Monitor {
  constructor () {
    this.model = new Model()
    this.view = new View()
  }

  async render () {
    const state = await this.model.getState()
    const section = await this.view.appendState(state)
    return section
  }

  afterRender () {
  }
}

export default Monitor
