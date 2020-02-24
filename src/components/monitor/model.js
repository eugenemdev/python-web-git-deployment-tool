import Service from '../../services/services.js'

/**
 * Model for component Home
 * @returns list of posts
 */

class Model {
  async getState () {
    const state = await new Service().getState()
    return state
  }
}

export default Model
