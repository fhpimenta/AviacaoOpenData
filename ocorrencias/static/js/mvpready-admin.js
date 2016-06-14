/* ========================================================
*
* MVP Ready - Lightweight & Responsive Admin Template
*
* ========================================================
*
* File: mvpready-admin.js
* Theme Version: 3.0.0
* Bootstrap Version: 3.3.6
* Author: Jumpstart Themes
* Website: http://mvpready.com
*
* ======================================================== */

var mvpready_admin = function () {

  "use strict"

  var initSearchField = function () {
    $('.navbar-search-field').focus (function (e) {
      $(this).parents ('form').addClass ('active')
      $(this).animate ({ width: '250px' })
    }).blur (function (e) {
      $(this).parents ('form').removeClass ('active')

      if (!$(this).val ()) {
        $(this).animate ({ width: '170px' })
      }
    })
  }

  return {
    init: function () {
      // Layouts
      mvpready_core.initNavHover ({ delay: { show: 250, hide: 350 } })

      initSearchField ()

      mvpready_core.initNavbarNotifications ()
      mvpready_core.initSidebarNav ()
      mvpready_core.initLayoutToggles ()
      mvpready_core.initBackToTop ()

      // Components
      mvpready_helpers.initAccordions ()
      mvpready_helpers.initFormValidation ()
      mvpready_helpers.initTooltips ()
      mvpready_helpers.initLightbox ()
      mvpready_helpers.initSelect ()
      mvpready_helpers.initIcheck ()
      mvpready_helpers.initDataTableHelper ()
      mvpready_helpers.initiTimePicker ()
      mvpready_helpers.initDatePicker ()
      mvpready_helpers.initColorPicker ()
    }
  }

}()

$(function () {
  mvpready_admin.init ()
})