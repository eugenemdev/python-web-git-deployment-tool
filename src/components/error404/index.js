'use strict'
/**
* Controller for component Error404
* @returns html to view error 404 then we have some error
*/
class Error404 {
  async render () {
    const view = /* html */`        
            <section class="section">
            <div class="page-wrap d-flex flex-row">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <span class="display-1 d-block">404</span>
                        <div class="mb-4 lead">The page  was not found.</div>
                        <a href="#/" class="btn btn-link">Back to Home</a>
                    </div>
                </div>
            </div>
            </div>
            </section>
        `
    return view
  }

  afterRender () {
  }
}
export default Error404
