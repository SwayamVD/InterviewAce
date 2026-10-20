---
version: alpha
name: Anthropic
description: "A warm, editorial, paper-and-ink system. Surfaces are off-white parchment (#FAF9F5) and soft clay-cream (#F0EEE6). Text is a near-black ink (#141413), and the footer inverts to an ink field with parchment text and stone-grey links. Typography pairs Anthropic Serif for reading copy and navigation with Anthropic Sans for headlines, labels and UI. There is a small Anthropic Mono accent. The accent strategy is restraint: no saturated brand hue. Hierarchy comes from ink-versus-paper contrast, a ladder of warm greys, and hairline borders. Rounded 8–16px cards, a single whisper-soft shadow and generous 48/96px section rhythm keep the feel calm and considered."
colors:
  primary: "#141413"
  on-primary: "#FAF9F5"
  ink: "#141413"
  ink-soft: "#30302E"
  body-muted: "#5E5D59"
  muted: "#73726C"
  muted-soft: "#87867F"
  on-dark-muted: "#B0AEA5"
  surface: "#FAF9F5"
  surface-alt: "#F0EEE6"
  surface-warm: "#E3DACC"
  surface-dark: "#141413"
  surface-dark-raised: "#3D3D3A"
  hairline: "#D1CFC5"
  on-dark: "#FAF9F5"
  black: "#000000"
  focus-ring: "#005FCC"
typography:
  hero-display:
    fontFamily: Anthropic Serif
    fontSize: 68.3429px
    fontWeight: 400
    lineHeight: 1.1
  display-lg:
    fontFamily: Anthropic Sans
    fontSize: 60.8653px
    fontWeight: 700
    lineHeight: 1.1
  display-md:
    fontFamily: Anthropic Sans
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
  headline:
    fontFamily: Anthropic Sans
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
  title-lg:
    fontFamily: Anthropic Sans
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
  body-lg:
    fontFamily: Anthropic Serif
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
  title-md:
    fontFamily: Anthropic Sans
    fontSize: 19px
    fontWeight: 600
    lineHeight: 1.2
  nav-link:
    fontFamily: Anthropic Serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.16px
  body-sans:
    fontFamily: Anthropic Sans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
  body:
    fontFamily: Anthropic Serif
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
  ui:
    fontFamily: Anthropic Sans
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
  button:
    fontFamily: Anthropic Sans
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.15px
  label:
    fontFamily: Anthropic Sans
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.15px
  caption:
    fontFamily: Anthropic Sans
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
  caption-medium:
    fontFamily: Anthropic Sans
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
  eyebrow:
    fontFamily: Anthropic Sans
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
rounded:
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
spacing:
  base: 4px
  section-padding-y: 48px
  header-inner-gap: 24px
  header-inner-inner-max-width: 1400px
  header-inner-mobile-gap: 24px
  header-inner-mobile-inner-max-width: 1400px
  header-inner-2-gap: 24px
  header-inner-2-inner-max-width: 1400px
  header-inner-2-mobile-gap: 24px
  header-inner-2-mobile-inner-max-width: 1400px
  header-inner-3-gap: 24px
  header-inner-3-inner-max-width: 1400px
  header-inner-3-mobile-gap: 24px
  header-inner-3-mobile-inner-max-width: 1400px
  card-3-grid-gap: 32px
  card-4-grid-gap: 16px
  button-primary-3-padding-y: 8px
  button-primary-3-padding-x: 16px
  button-secondary-padding-y: 8px
  button-secondary-padding-x: 16px
  button-ghost-2-padding-y: 8px
  button-ghost-2-padding-left: 24px
  button-ghost-2-padding-right: 16px
  input-padding-y: 8px
  input-padding-left: 40px
  input-padding-right: 16px
  button-secondary-3-padding-y: 8px
  button-secondary-3-padding-left: 24px
  button-secondary-3-padding-right: 16px
  button-ghost-4-padding-y: 4px
  button-ghost-4-padding-left: 8px
  button-ghost-4-padding-right: 12px
components:
  button-primary:
    textColor: "#141413"
    typography:
      fontFamily: '"Anthropic Serif", Georgia, sans-serif'
      fontSize: 20px
      fontWeight: 400
      lineHeight: 28px
    height: 36px
  button-primary-group:
    backgroundColor: "#141413"
    textColor: "#FAF9F5"
  button-primary-label:
    textColor: "#FAF9F5"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 16px
      fontWeight: 400
      lineHeight: 16px
      letterSpacing: -0.08px
  button-ghost:
    backgroundColor: transparent
    textColor: "#B0AEA5"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 12px
      fontWeight: 400
      lineHeight: 16.8px
      letterSpacing: -0.24px
    height: 17px
  button-ghost-hover:
    textColor: "#FAF9F5"
  card:
    textColor: "#141413"
    typography:
      fontFamily: '"Anthropic Serif", Georgia, sans-serif'
      fontSize: 20px
      fontWeight: 400
      lineHeight: 28px
    height: 559px
  card-group:
    rounded: 16px
    padding: 31.4776px
  card-group-2:
    backgroundColor: "#E3DACC"
  card-title:
    textColor: "#141413"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 24px
      fontWeight: 600
      lineHeight: 31.2px
  card-body:
    textColor: "#141413"
    typography:
      fontFamily: '"Anthropic Serif", Georgia, sans-serif'
      fontSize: 18px
      fontWeight: 400
      lineHeight: 25.2px
  card-group-7:
    backgroundColor: "#141413"
    textColor: "#FAF9F5"
    rounded: 8px
  nav-menu:
    textColor: "#141413"
    height: 68px
  nav-menu-link:
    textColor: "#141413"
    height: 69px
    width: 65px
  nav-menu-2:
    textColor: "#FAF9F5"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 12px
      fontWeight: 400
      lineHeight: 16.8px
    height: 829px
  nav-menu-2-icon:
    height: 32px
    width: 45px
  nav-menu-2-text:
    textColor: "#B0AEA5"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 12px
      fontWeight: 400
      lineHeight: 16.8px
  nav-menu-2-title:
    textColor: "#FAF9F5"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 12px
      fontWeight: 500
      lineHeight: 16.8px
  hero:
    textColor: "#141413"
    height: 390px
  nav-dropdown:
    textColor: "#141413"
    typography:
      fontFamily: '"Anthropic Serif", Georgia, sans-serif'
      fontSize: 20px
      fontWeight: 400
      lineHeight: 28px
    height: 69px
  nav-dropdown-text:
    textColor: "#141413"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  nav-dropdown-icon:
    height: 24px
    width: 12px
  nav-dropdown-2:
    textColor: "#141413"
    typography:
      fontFamily: '"Anthropic Serif", Georgia, sans-serif'
      fontSize: 20px
      fontWeight: 400
      lineHeight: 28px
    height: 69px
  nav-dropdown-2-text:
    textColor: "#141413"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  nav-dropdown-2-icon:
    height: 24px
    width: 12px
  nav-dropdown-3:
    textColor: "#141413"
    typography:
      fontFamily: '"Anthropic Serif", Georgia, sans-serif'
      fontSize: 20px
      fontWeight: 400
      lineHeight: 28px
    height: 69px
  nav-dropdown-3-text:
    textColor: "#141413"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  nav-dropdown-3-icon:
    height: 24px
    width: 12px
  header-landing:
    backgroundColor: "#F0EEE6"
    textColor: "#141413"
    typography:
      fontFamily: '"Anthropic Serif", Georgia, sans-serif'
      fontSize: 20px
      fontWeight: 400
      lineHeight: 28px
    height: 68px
  header-landing-logo:
    textColor: "#141413"
    height: 68px
    width: 144px
  header-landing-logo-icon:
    height: 16px
    width: 143px
  header-landing-text:
    textColor: "#141413"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  header-landing-nav-link:
    textColor: "#141413"
  header-landing-group-6:
    backgroundColor: "#141413"
    textColor: "#FAF9F5"
  header-landing-text-2:
    textColor: "#FAF9F5"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 15px
      fontWeight: 400
      lineHeight: 15px
      letterSpacing: -0.08px
  header-landing-cta:
    textColor: "#141413"
    typography:
      fontFamily: '"Anthropic Serif", Georgia, sans-serif'
      fontSize: 20px
      fontWeight: 400
      lineHeight: 28px
    height: 36px
  header-landing-logo-hover:
    textColor: "#5E5D59"
  footer-landing:
    backgroundColor: "#141413"
    textColor: "#FAF9F5"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 12px
      fontWeight: 400
      lineHeight: 16.8px
    height: 981px
  footer-landing-heading:
    textColor: "#FAF9F5"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 12px
      fontWeight: 400
      lineHeight: 16.8px
  footer-landing-icon:
    height: 32px
    width: 45px
  footer-landing-group-3:
    textColor: "#B0AEA5"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 12px
      fontWeight: 400
      lineHeight: 16.8px
  footer-landing-text-2:
    textColor: "#B0AEA5"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 12px
      fontWeight: 400
      lineHeight: 16.8px
  footer-landing-nav-link:
    textColor: "#B0AEA5"
    size: 24px
  footer-landing-column-heading:
    textColor: "#FAF9F5"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 12px
      fontWeight: 500
      lineHeight: 16.8px
  footer-landing-nav-link-2:
    textColor: "#B0AEA5"
    height: 17px
    width: 39px
  footer-landing-nav-link-hover:
    textColor: "#FAF9F5"
  footer-landing-nav-link-2-hover:
    textColor: "#FAF9F5"
  footer-landing-mobile:
    backgroundColor: "#141413"
    textColor: "#FAF9F5"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 12px
      fontWeight: 400
      lineHeight: 16.8px
    height: 3188px
  footer-landing-mobile-heading:
    textColor: "#FAF9F5"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 12px
      fontWeight: 400
      lineHeight: 16.8px
  footer-landing-mobile-icon:
    height: 32px
    width: 45px
  footer-landing-mobile-column-heading:
    textColor: "#FAF9F5"
    typography:
      fontFamily: '"Anthropic Sans", Arial, sans-serif'
      fontSize: 12px
      fontWeight: 500
      lineHeight: 16.8px
  footer-landing-mobile-nav-link:
    textColor: "#B0AEA5"
    height: 17px
    width: 39px
  footer-landing-mobile-nav-link-hover:
    textColor: "#FAF9F5"
  button-primary-2:
    backgroundColor: "#0F0F0E"
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
    height: 36px
  button-primary-2-hover:
    backgroundColor: "#000000CC"
  button-primary-3:
    backgroundColor: "#141413"
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    rounded: 8px
    height: 40px
  button-primary-3-label:
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
  button-primary-3-hover:
    backgroundColor: "#3D3D3A"
  button-secondary:
    textColor: "#141413"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    rounded: 8px
    height: 40px
  button-secondary-label:
    textColor: "#141413"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
  button-secondary-hover:
    backgroundColor: "#141413"
    textColor: "#FAF9F5"
  button-secondary-2:
    backgroundColor: "#FAF9F5"
    textColor: "#141413"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    rounded: 8px
    height: 36px
  button-secondary-2-label:
    textColor: "#141413"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
  button-secondary-2-icon:
    size: 20px
  button-secondary-2-hover:
    backgroundColor: "#F0EEE6"
  card-2:
    textColor: "#141413"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    height: 87px
  card-2-link:
    textColor: "#0F0F0E"
  card-2-title:
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 32px
      fontWeight: 600
      lineHeight: 38.4px
  card-2-text:
    textColor: "#141413"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 17px
      fontWeight: 400
      lineHeight: 26.35px
  footer-nav:
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    height: 975px
  footer-nav-title:
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 12px
      fontWeight: 700
      lineHeight: 16.8px
  nav-dropdown-4:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
    height: 21px
  nav-dropdown-4-icon:
    height: 6px
    width: 12px
  nav-dropdown-5:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
    height: 21px
  nav-dropdown-5-icon:
    height: 6px
    width: 12px
  nav-dropdown-6:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
    height: 21px
  nav-dropdown-6-icon:
    height: 6px
    width: 12px
  social-link:
    textColor: "#FAF9F5"
    height: 24px
  social-link-link:
    textColor: "#141413"
    height: 20px
    width: 24px
  social-link-icon:
    size: 24px
  header-inner:
    backgroundColor: "#FAF9F5"
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    height: 68px
  header-inner-logo:
    textColor: "#141413"
    height: 16px
    width: 143px
  header-inner-logo-icon:
    height: 16px
    width: 143px
  header-inner-button:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  header-inner-button-icon:
    height: 6px
    width: 12px
  header-inner-nav-link:
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  header-inner-cta:
    backgroundColor: "#0F0F0E"
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
    height: 36px
  header-inner-group-5:
    backgroundColor: "#0F0F0E"
    textColor: "#FAF9F5"
  header-inner-icon:
    height: 6px
    width: 12px
  header-inner-logo-hover:
    textColor: "#87867F"
  header-inner-logo-focus:
    textColor: "#87867F"
  header-inner-cta-hover:
    backgroundColor: "#000000CC"
  footer-inner:
    backgroundColor: "#141413"
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    height: 1103px
  footer-inner-columns:
    padding: 64px
  footer-inner-link:
    textColor: "#141413"
    height: 20px
    width: 46px
  footer-inner-link-icon:
    height: 32px
    width: 46px
  footer-inner-heading:
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 12px
      fontWeight: 700
      lineHeight: 16.8px
  footer-inner-nav-link:
    textColor: "#B0AEA5"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 12px
      fontWeight: 400
      lineHeight: 16.8px
  footer-inner-link-focus:
    textColor: "#87867F"
  footer-inner-nav-link-hover:
    textColor: "#FFFFFF"
  header-inner-mobile:
    backgroundColor: "#FAF9F5"
    textColor: "#0F0F0E"
    height: 64px
  header-inner-mobile-logo:
    textColor: "#141413"
    size: 32px
  header-inner-mobile-logo-icon:
    size: 32px
  header-inner-mobile-menu-toggle:
    backgroundColor: transparent
    textColor: "#141413"
    size: 24px
  header-inner-mobile-menu-toggle-icon:
    size: 24px
  header-inner-mobile-logo-hover:
    textColor: "#87867F"
  header-inner-mobile-logo-focus:
    textColor: "#87867F"
  footer-inner-mobile:
    backgroundColor: "#141413"
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    height: 3651px
  footer-inner-mobile-inner:
    padding: 32px
  footer-inner-mobile-link:
    textColor: "#141413"
    height: 20px
    width: 46px
  footer-inner-mobile-link-icon:
    height: 32px
    width: 46px
  footer-inner-mobile-heading:
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 12px
      fontWeight: 700
      lineHeight: 16.8px
  footer-inner-mobile-nav-link:
    textColor: "#B0AEA5"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 12px
      fontWeight: 400
      lineHeight: 16.8px
  footer-inner-mobile-link-hover:
    textColor: "#87867F"
  footer-inner-mobile-link-focus:
    textColor: "#87867F"
  footer-inner-mobile-nav-link-hover:
    textColor: "#FFFFFF"
  button-ghost-2:
    backgroundColor: "#F5F4ED"
    textColor: "#73726C"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    rounded: 8px
    height: 40px
  button-ghost-2-label:
    textColor: "#73726C"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
  button-ghost-2-icon:
    height: 16px
    width: 17px
  button-ghost-3:
    backgroundColor: transparent
    textColor: "#B0AEA5"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 12px
      fontWeight: 400
      lineHeight: 16.8px
    height: 17px
  button-ghost-3-focus:
    textColor: "#FFFFFF"
  input:
    backgroundColor: "#FFFFFF"
    textColor: "#141413"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 14px
      fontWeight: 400
      lineHeight: 14px
    rounded: 12px
    height: 44px
    width: 294px
  card-3:
    textColor: "#141413"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    height: 157px
  card-3-title:
    textColor: "#141413"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 19px
      fontWeight: 600
      lineHeight: 22.8px
  card-3-body:
    textColor: "#141413"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
  footer-navigation:
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    height: 975px
  footer-navigation-title:
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 12px
      fontWeight: 700
      lineHeight: 16.8px
  navigation-menu:
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    height: 21px
  navigation-menu-button:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  navigation-menu-icon:
    height: 6px
    width: 12px
  navigation-menu-link:
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  navigation-menu-2:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
    height: 21px
  navigation-menu-2-icon:
    height: 6px
    width: 12px
  navigation-menu-3:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
    height: 21px
  navigation-menu-3-icon:
    height: 6px
    width: 12px
  button-secondary-3:
    backgroundColor: "#F5F4ED"
    textColor: "#73726C"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    rounded: 8px
    height: 40px
  button-secondary-3-label:
    textColor: "#73726C"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
  button-secondary-3-icon:
    height: 16px
    width: 17px
  button-secondary-3-hover:
    backgroundColor: "#E8E6DC"
  button-ghost-4:
    backgroundColor: "#F5F4ED"
    textColor: "#73726C"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    rounded: 6px
    height: 28px
  button-ghost-4-label:
    textColor: "#73726C"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 14px
      fontWeight: 400
      lineHeight: 16.8px
      letterSpacing: 0.15px
  button-ghost-4-icon:
    size: 20px
  button-ghost-4-hover:
    backgroundColor: "#E8E6DC"
  footer-link-column:
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    height: 975px
  footer-link-column-title:
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 12px
      fontWeight: 700
      lineHeight: 16.8px
  navigation-dropdown:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
    height: 21px
  navigation-dropdown-icon:
    height: 6px
    width: 12px
  navigation-dropdown-2:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
    height: 21px
  navigation-dropdown-2-icon:
    height: 6px
    width: 12px
  navigation-dropdown-3:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
    height: 21px
  navigation-dropdown-3-icon:
    height: 6px
    width: 12px
  legal-text:
    textColor: "#B0AEA5"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 12px
      fontWeight: 400
      lineHeight: 16.8px
    height: 34px
  nav-menu-3:
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    height: 21px
  nav-menu-3-button:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  nav-menu-3-icon:
    height: 6px
    width: 12px
  nav-menu-3-link:
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  header-inner-2:
    backgroundColor: "#FAF9F5"
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    height: 68px
  header-inner-2-logo:
    textColor: "#141413"
    height: 16px
    width: 143px
  header-inner-2-logo-icon:
    height: 16px
    width: 143px
  header-inner-2-button:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  header-inner-2-button-icon:
    height: 6px
    width: 12px
  header-inner-2-nav-link:
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  header-inner-2-button-icon-2:
    height: 6px
    width: 12px
  header-inner-2-group-4:
    backgroundColor: "#FAF9F5"
    rounded: 16px
    padding: 24px
  header-inner-2-text-2:
    textColor: "#5E5D59"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 14px
      fontWeight: 400
      lineHeight: 16.8px
      letterSpacing: 0.15px
  header-inner-2-cta:
    backgroundColor: "#0F0F0E"
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
    height: 36px
  header-inner-2-group-8:
    backgroundColor: "#0F0F0E"
    textColor: "#FAF9F5"
  header-inner-2-icon:
    height: 6px
    width: 12px
  header-inner-2-logo-hover:
    textColor: "#87867F"
  header-inner-2-logo-focus:
    textColor: "#87867F"
  header-inner-2-cta-hover:
    backgroundColor: "#000000CC"
  header-inner-2-mobile:
    backgroundColor: "#FAF9F5"
    textColor: "#0F0F0E"
    height: 64px
  header-inner-2-mobile-logo:
    textColor: "#141413"
    size: 32px
  header-inner-2-mobile-logo-icon:
    size: 32px
  header-inner-2-mobile-menu-toggle:
    backgroundColor: transparent
    textColor: "#141413"
    size: 24px
  header-inner-2-mobile-menu-toggle-icon:
    size: 24px
  header-inner-2-mobile-logo-hover:
    textColor: "#87867F"
  header-inner-2-mobile-logo-focus:
    textColor: "#87867F"
  button-ghost-5:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
    height: 21px
  button-ghost-5-icon:
    height: 6px
    width: 12px
  button-ghost-6:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
    height: 21px
  button-ghost-6-icon:
    height: 6px
    width: 12px
  card-4:
    textColor: "#141413"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
  card-4-text:
    textColor: "#141413"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 14px
      fontWeight: 500
      lineHeight: 16.8px
      letterSpacing: 0.15px
  card-4-text-2:
    textColor: "#5E5D59"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 14px
      fontWeight: 500
      lineHeight: 16.8px
      letterSpacing: 0.15px
  card-4-title:
    textColor: "#141413"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 19px
      fontWeight: 600
      lineHeight: 22.8px
  card-4-body:
    textColor: "#141413"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
  nav:
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    height: 21px
  nav-button:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  nav-icon:
    height: 6px
    width: 12px
  nav-link:
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  nav-2:
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    height: 975px
  nav-2-title:
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 12px
      fontWeight: 700
      lineHeight: 16.8px
  video:
    backgroundColor: transparent
    textColor: "#000000"
    height: 358px
  video-media:
    height: 358px
    width: 636px
  video-group:
    backgroundColor: "#0F0F0E"
    textColor: "#FFFFFF"
    rounded: 16px
    padding: 16px
  video-icon:
    size: 22px
  video-2:
    backgroundColor: transparent
    textColor: "#000000"
    height: 471px
  video-2-media:
    height: 471px
    width: 837px
  video-2-group:
    backgroundColor: "#0F0F0E"
    textColor: "#FFFFFF"
    rounded: 16px
    padding: 16px
  video-2-icon:
    size: 22px
  header-inner-3:
    backgroundColor: "#FAF9F5"
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSerif, "anthropicSerif Fallback", serif
      fontSize: 16px
      fontWeight: 400
      lineHeight: 20px
      letterSpacing: -0.16px
    height: 68px
  header-inner-3-logo:
    textColor: "#141413"
    height: 16px
    width: 143px
  header-inner-3-logo-icon:
    height: 16px
    width: 143px
  header-inner-3-cta:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
    height: 21px
  header-inner-3-cta-icon:
    height: 6px
    width: 12px
  header-inner-3-nav-link:
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  header-inner-3-button:
    backgroundColor: transparent
    textColor: "#0F0F0E"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
      letterSpacing: -0.0375px
  header-inner-3-button-icon:
    height: 6px
    width: 12px
  header-inner-3-cta-2:
    backgroundColor: "#0F0F0E"
    textColor: "#FAF9F5"
    typography:
      fontFamily: anthropicSans, "anthropicSans Fallback", sans-serif
      fontSize: 15px
      fontWeight: 400
      lineHeight: 21px
    height: 36px
  header-inner-3-group-5:
    backgroundColor: "#0F0F0E"
    textColor: "#FAF9F5"
  header-inner-3-icon:
    height: 6px
    width: 12px
  header-inner-3-logo-hover:
    textColor: "#87867F"
  header-inner-3-logo-focus:
    textColor: "#87867F"
  header-inner-3-cta-2-hover:
    backgroundColor: "#000000CC"
  header-inner-3-mobile:
    backgroundColor: "#FAF9F5"
    textColor: "#0F0F0E"
    height: 64px
  header-inner-3-mobile-logo:
    textColor: "#141413"
    size: 32px
  header-inner-3-mobile-logo-icon:
    size: 32px
  header-inner-3-mobile-menu-toggle:
    backgroundColor: transparent
    textColor: "#141413"
    size: 24px
  header-inner-3-mobile-menu-toggle-icon:
    size: 24px
  header-inner-3-mobile-logo-focus:
    textColor: "#87867F"
---

# Anthropic

## Overview

Anthropic's site reads like a well-set research journal printed on warm paper. The canvas is **Parchment** (`surface`, #FAF9F5), text is a near-black **Ink** (`ink`, #141413), and there is no saturated brand hue at all. Every accent is either ink-on-paper or paper-on-ink. A small ladder of warm stone greys carries secondary information. The footer is the one place the page inverts to a full ink field.

Density is low and deliberate. Sections breathe on a `section-padding-y` rhythm, and lists are set as ruled rows rather than boxed cards. Content sits inside a wide container that never feels crowded. The personality is editorial, not techy. A bookish serif (Anthropic Serif) carries navigation, intros and reading copy. A firm grotesque (Anthropic Sans) carries headlines, labels and UI chrome. That role split is itself a hierarchy tool: serif means "read this", sans means "scan or act on this".

Hierarchy comes from four things, in this order:

1. Size and weight jumps in the sans display ladder.
2. Ink-versus-grey value contrast.
3. Tonal surface changes between parchment, clay-cream and tan.
4. 1px hairlines.

Shadows exist, but only on floating elements such as the nav dropdown panel and the video play control. They are never used to structure the page.

**Key Characteristics:**

- Warm, achromatic palette: parchment, clay-cream and tan surfaces with ink text, and zero brand color.
- Serif/sans role split: `body-lg`, `body` and `nav-link` are serif; every display, headline, title and label token is sans.
- Solid ink buttons (`button-primary-3`, #141413 fill, `rounded.sm`) are the strongest contrast point on any light page.
- Lists are built from hairline-ruled rows (`card-2` bottom border #87867F; `card-4` hover border `hairline`) rather than boxed tiles.
- Tan feature cards (`surface-warm`, #E3DACC) at `rounded.lg` are the main tonal accent.
- A full-bleed ink footer (`surface-dark`) with parchment headings and stone links (`on-dark-muted`, #B0AEA5).
- Shadows only for floating layers: a three-layer whisper shadow on the dropdown panel and a single soft shadow on the video control.
- Focus is shown with a 2px outline in the current text color, not a colored ring.

## Colors

The palette is a warm greyscale: paper tones, ink, and a stepped ladder of stone greys. There are no gradients anywhere on the site, and there is no chromatic accent in the page palette.

### Brand & Ink

- **Ink** (`primary`, #141413): the brand color is ink itself. Use it for primary button fills (`button-primary-3`), headlines, body text and focus outlines on light surfaces.
- **Ink** (`ink`, #141413): the default text color for everything on parchment.
- **Graphite** (`ink-soft`, #30302E): a rare softened ink for secondary dark text. It is barely used; do not promote it to a main role.
- **Paper-on-Ink** (`on-primary`, #FAF9F5): label color on ink buttons and the CTA in the header.
- **Pure Black** (`black`, #000000): appears only in media and video contexts. Never use it for text or UI on parchment, because Ink is the system black.

### Surface

- **Parchment** (`surface`, #FAF9F5): the default page and header canvas (`header-inner` background). It is also the fill of the nav dropdown panel (`header-inner-2-group-4`).
- **Clay Cream** (`surface-alt`, #F0EEE6): the alternate band and landing-header fill (`header-landing` background). It is also the hover fill of `button-secondary-2` (flagged: the `button-secondary-2-icon` x did not reproduce the measured 128px after 2 correction attempts).
- **Tan** (`surface-warm`, #E3DACC): the feature-card fill (`card-group-2` in `card`, flagged: the `card-group` height did not reproduce the measured 559px after 2 correction attempts). It is the warmest tone in the system; reserve it for highlighted cards.
- **Ink Field** (`surface-dark`, #141413): the footer background (`footer-inner`, `footer-landing`) and the dark CTA band.
- **Raised Ink** (`surface-dark-raised`, #3D3D3A): measured only on components. It is the hover fill of `button-primary-3` and the left border of the split button group in `button-primary` (flagged: the render matched 59% of the original pixels, below the 97% required on hover after 2 correction attempts).

### Text Greys (light surfaces)

- **Driftwood** (`body-muted`, #5E5D59): secondary metadata such as the dates in `card-4-text-2` and the dropdown descriptions in `header-inner-2-text-2`. It is also the logo hover in `header-landing`.
- **Stone** (`muted`, #73726C): labels inside the soft ghost and secondary buttons (`button-ghost-2`, `button-secondary-3`, `button-ghost-4`).
- **Pebble** (`muted-soft`, #87867F): the logo hover and focus state (`header-inner-logo-hover`), the row rule under `card-2`, and the input focus border.

### Text on Dark

- **Paper** (`on-dark`, #FAF9F5): footer headings and column titles (`footer-inner-heading`).
- **Ash** (`on-dark-muted`, #B0AEA5): footer links (`footer-inner-nav-link`) and legal text (`legal-text`). These links brighten to #FFFFFF on hover.

### Hairlines & Borders

- **Hairline** (`hairline`, #D1CFC5): the 1px border on `input`, `button-ghost-2`, `button-secondary-3` and `button-ghost-4`, and the row rule that appears on `card-4` hover and focus. This is the only neutral divider token.

### Component & State Colors (recipe-only)

These were measured on components, not in the page sampling. Keep them scoped to the components named.

| Value     | Where it lives                                                                                                                                                                    |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| #F5F4ED   | Resting fill of `button-ghost-2`, `button-secondary-3` and `button-ghost-4`, a hair lighter than `surface-alt`                                                                    |
| #E8E6DC   | Hover fill of `button-secondary-3` and `button-ghost-4`; also the divider under `header-inner-2-group-5`                                                                          |
| #0F0F0E   | Fill of the header CTA `button-primary-2` (flagged: the render matched 96% of the original pixels, below the 97% required after 2 correction attempts), which hovers to #000000CC |
| #FFFFFF   | The `input` field fill                                                                                                                                                            |
| #FFFFFF33 | The divider inside the split header CTA (`header-inner-group-5`)                                                                                                                  |

- **Focus Blue** (`focus-ring`, #005FCC): a single focus measurement from the recipes. Visible focus on the measured components is actually drawn as a 2px outline in #141413 on light surfaces and #FAF9F5 on dark surfaces. Treat `focus-ring` as a fallback, not the house style.

## Typography

### Font Family

- **Anthropic Serif** is the reading and navigation voice. It carries the hero display (`hero-display`), the intro paragraph (`body-lg`), paragraph copy (`body`) and serif link text (`nav-link`). Its fallback stack is Georgia/serif.
- **Anthropic Sans** is the structural voice. It carries every headline and display size, card titles, nav buttons, button labels, metadata and the entire footer. Its fallback stack is Arial/sans-serif.
- **Anthropic Mono** appears only as a trace accent, measured on a single page. It has no token, so do not build with it unless you are reproducing tabular metadata labels.

### Hierarchy

| Token            | Size      | Weight | Line Height | Letter Spacing | Use                                                            |
| ---------------- | --------- | ------ | ----------- | -------------- | -------------------------------------------------------------- |
| `hero-display`   | 68.3429px | 400    | 1.1         | normal         | Serif home-hero statement                                      |
| `display-lg`     | 60.8653px | 700    | 1.1         | normal         | Sans H1 headline                                               |
| `display-md`     | 52px      | 700    | 1.1         | normal         | Page H1/H2 on inner pages                                      |
| `headline`       | 32px      | 600    | 1.2         | normal         | Section H2 and list-row titles (`card-2-title`)                |
| `title-lg`       | 24px      | 600    | 1.3         | normal         | Feature card titles (`card-title`)                             |
| `body-lg`        | 20px      | 400    | 1.4         | normal         | Serif hero intro and lead paragraphs                           |
| `title-md`       | 19px      | 600    | 1.2         | normal         | Small card and article titles (`card-3-title`, `card-4-title`) |
| `nav-link`       | 16px      | 400    | 1.25        | -0.16px        | Serif inline and list links                                    |
| `body-sans`      | 16px      | 400    | 1.4         | normal         | Sans list and link copy                                        |
| `body`           | 15px      | 400    | 1.4         | normal         | Serif paragraph copy (`card-3-body`, `card-4-body`)            |
| `ui`             | 15px      | 400    | 1.4         | normal         | Nav buttons, dropdown triggers, button labels                  |
| `button`         | 14px      | 500    | 1.2         | 0.15px         | Compact button labels                                          |
| `label`          | 14px      | 400    | 1.2         | 0.15px         | Metadata and dropdown descriptions (`header-inner-2-text-2`)   |
| `caption`        | 12px      | 400    | 1.4         | normal         | Footer links and legal text                                    |
| `caption-medium` | 12px      | 500    | 1.4         | normal         | Footer column headings (landing variant)                       |
| `eyebrow`        | 12px      | 700    | 1.4         | normal         | Footer section titles (`footer-inner-heading`)                 |

### Principles

- **Serif reads, sans structures.** Never set a headline in the serif except the single `hero-display` statement. Never set a long paragraph in the sans except list descriptions.
- **Four weights, with clear jobs.**
  - 400 is all reading text.
  - 500 is compact labels (`button`, `caption-medium`).
  - 600 is titles (`headline`, `title-lg`, `title-md`).
  - 700 is reserved for the big display sizes and the tiny `eyebrow`.
  - The hero serif stays at 400; weight never carries the serif's hierarchy.
- **Tight displays, open text.** Display sizes sit at 1.1, titles at 1.2–1.3, and reading copy at 1.4.
- **Letter-spacing is micro and directional.** The serif `nav-link` tightens by -0.16px. The small sans `button` and `label` open by 0.15px for legibility. Everything else stays normal. Never track headlines.
- **Odd display sizes are real.** 68.3429px and 60.8653px come from fluid scaling. Keep them as tokens rather than rounding them.

### Note on Font Substitutes

All three families are proprietary.

| Proprietary family | Open-source stand-in                                      | How to tune it                                                                                                                                            |
| ------------------ | --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anthropic Sans     | Inter, or Instrument Sans for a slightly warmer grotesque | Tighten displays by roughly -1% to -2% at `display-lg` and `display-md`; keep 600/700 weights for titles                                                  |
| Anthropic Serif    | Source Serif 4 or Newsreader                              | Set `body` at the same 15px. Check the x-height: if the stand-in runs large, drop it about 0.5px so line lengths match. Keep `hero-display` at weight 400 |
| Anthropic Mono     | JetBrains Mono                                            | Use it only for uppercase metadata labels                                                                                                                 |

## Layout

### Spacing System

Everything snaps to a 4px step (`base`, 4px). The vertical rhythm between page sections is `section-padding-y` (48px). It was measured on the page itself across repeated section edges, not on any component.

| Token                                                               | Value             | Read on                                                                                                  |
| ------------------------------------------------------------------- | ----------------- | -------------------------------------------------------------------------------------------------------- |
| `base`                                                              | 4px               | Common step of all verified paddings and gaps                                                            |
| `section-padding-y`                                                 | 48px              | Page section top and bottom padding                                                                      |
| `header-inner-gap`                                                  | 24px              | Gap between nav and CTA groups in `header-inner` (same in `header-inner-2-gap` and `header-inner-3-gap`) |
| `header-inner-mobile-gap`                                           | 24px              | Gap between logo-side and toggle groups in the mobile header                                             |
| `card-3-grid-gap`                                                   | 32px              | Column gap of the team-summary card grid                                                                 |
| `card-4-grid-gap`                                                   | 16px              | Gap between stacked article rows                                                                         |
| `button-primary-3-padding-y` / `-padding-x`                         | 8px / 16px        | Solid ink button                                                                                         |
| `button-secondary-padding-y` / `-padding-x`                         | 8px / 16px        | Outlined ink button                                                                                      |
| `button-ghost-2-padding-y` / `-padding-left` / `-padding-right`     | 8px / 24px / 16px | Soft icon button (icon leads)                                                                            |
| `button-secondary-3-padding-y` / `-padding-left` / `-padding-right` | 8px / 24px / 16px | Soft secondary button with icon                                                                          |
| `button-ghost-4-padding-y` / `-padding-left` / `-padding-right`     | 4px / 8px / 12px  | Compact chip-like ghost button                                                                           |
| `input-padding-y` / `-padding-left` / `-padding-right`              | 8px / 40px / 16px | Search input; the 40px left leaves room for a leading icon                                               |

### Grid & Container

- **Container.** Content is capped by the header's inner container at `header-inner-inner-max-width` (1400px). The same cap repeats in every header variant (`header-inner-2-inner-max-width`, `header-inner-3-inner-max-width`, and the mobile equivalents). Treat 1400px as the site-wide max width.
- **Grid gaps.** Card grids use `card-3-grid-gap` (32px). Tight stacked lists use `card-4-grid-gap` (16px).
- **Column patterns in the screenshots:**
  - The hero splits a large left headline from a right-hand serif intro.
  - Release cards run as an equal-width row.
  - List sections pair a left heading column with a right column of hairline-ruled rows.
  - The research page uses a multi-up team summary and a feature image with a stacked article list beside it.
  - The footer is a multi-column link directory.

### Whitespace Philosophy

Whitespace does the work that boxes and shadows do elsewhere:

- Sections are separated by `section-padding-y` and tonal band changes, not by divider lines.
- Button padding is compact (`button-primary-3-padding-y`, `button-primary-3-padding-x`), so controls stay quiet next to large headlines.

When in doubt, add vertical space in `base` multiples rather than adding a container.

### Measured Layout

Every spacing token restates a measurement of a verified component recipe, or the step those measurements share. `section-padding-y` is measured directly on the page sections and feeds no step.

- `base`: 4px (greatest common step of the verified component paddings and gaps: 24px, 32px, 16px, 8px, 40px, 4px, 12px)
- `section-padding-y`: 48px (vertical padding repeated on the page sections: 14 section edges on 4 pages)
- `header-inner-gap`: 24px (`header-inner`, gap of `header-inner-group-3`)
- `header-inner-inner-max-width`: 1400px (`header-inner`, max width of `header-inner-inner`)
- `header-inner-mobile-gap`: 24px (`header-inner-mobile`, gap of `header-inner-mobile-group`)
- `header-inner-mobile-inner-max-width`: 1400px (`header-inner-mobile`, max width of `header-inner-mobile-inner`)
- `header-inner-2-gap`: 24px (`header-inner-2`, gap of `header-inner-2-group-3`)
- `header-inner-2-inner-max-width`: 1400px (`header-inner-2`, max width of `header-inner-2-inner`)
- `header-inner-2-mobile-gap`: 24px (`header-inner-2-mobile`, gap of `header-inner-2-mobile-group`)
- `header-inner-2-mobile-inner-max-width`: 1400px (`header-inner-2-mobile`, max width of `header-inner-2-mobile-inner`)
- `header-inner-3-gap`: 24px (`header-inner-3`, gap of `header-inner-3-group-3`)
- `header-inner-3-inner-max-width`: 1400px (`header-inner-3`, max width of `header-inner-3-inner`)
- `header-inner-3-mobile-gap`: 24px (`header-inner-3-mobile`, gap of `header-inner-3-mobile-group`)
- `header-inner-3-mobile-inner-max-width`: 1400px (`header-inner-3-mobile`, max width of `header-inner-3-mobile-inner`)
- `card-3-grid-gap`: 32px (`card-3`, column gap of the grid its instances sit in)
- `card-4-grid-gap`: 16px (`card-4`, column gap of the grid its instances sit in)
- `button-primary-3-padding-y`: 8px (`button-primary-3`, vertical padding of the root)
- `button-primary-3-padding-x`: 16px (`button-primary-3`, horizontal padding of the root)
- `button-secondary-padding-y`: 8px (`button-secondary`, vertical padding of the root)
- `button-secondary-padding-x`: 16px (`button-secondary`, horizontal padding of the root)
- `button-ghost-2-padding-y`: 8px (`button-ghost-2`, vertical padding of the root)
- `button-ghost-2-padding-left`: 24px (`button-ghost-2`, left padding of the root)
- `button-ghost-2-padding-right`: 16px (`button-ghost-2`, right padding of the root)
- `input-padding-y`: 8px (`input`, vertical padding of the root)
- `input-padding-left`: 40px (`input`, left padding of the root)
- `input-padding-right`: 16px (`input`, right padding of the root)
- `button-secondary-3-padding-y`: 8px (`button-secondary-3`, vertical padding of the root)
- `button-secondary-3-padding-left`: 24px (`button-secondary-3`, left padding of the root)
- `button-secondary-3-padding-right`: 16px (`button-secondary-3`, right padding of the root)
- `button-ghost-4-padding-y`: 4px (`button-ghost-4`, vertical padding of the root)
- `button-ghost-4-padding-left`: 8px (`button-ghost-4`, left padding of the root)
- `button-ghost-4-padding-right`: 12px (`button-ghost-4`, right padding of the root)

The card-3 grid lays out in 5 columns at desktop.

## Elevation & Depth

| Level         | Treatment                                                                                                                | Use                                                                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Flat / tonal  | No shadow. Depth from surface change: `surface` → `surface-alt` → `surface-warm`, with `surface-dark` for full inversion | Page bands, tan feature cards (`card-group-2`), footer                                                                                                         |
| Hairline      | 1px solid `hairline` (#D1CFC5); row rules in #87867F (`card-2`) and #1414131A (`card-list`)                              | Inputs, soft buttons, list rows, metadata rows                                                                                                                 |
| Outline focus | 2px solid #141413 at -2px offset on light surfaces; 2px solid #FAF9F5 at 4px offset on dark                              | Keyboard focus on nav links, logo, dropdowns and footer links                                                                                                  |
| Soft lift     | `#0000000D 0px 4px 24px 0px`                                                                                             | Play control over video thumbnails (`video-group`, flagged: the render matched 46% of the original pixels, below the 96% required after 2 correction attempts) |
| Layered panel | `#00000003 0px 2px 2px 0px, #00000005 0px 4px 4px 0px, #0000000A 0px 16px 24px 0px`, plus a 1px #F0EEE6 border           | Nav dropdown panel (`header-inner-2-group-4`): `surface` fill, `rounded.lg`, 24px padding                                                                      |
| Blur          | None measured                                                                                                            | —                                                                                                                                                              |

**Shadow philosophy.** The page itself is built tonally: bands, cards and lists never cast shadows. Lift is reserved for things that genuinely float above the page, and there are exactly two such treatments.

- **Layered panel shadow.** The dropdown panel uses a three-step shadow whose alphas climb from 0x03 to 0x0A as the blur widens. The result is an atmospheric, almost invisible lift; pair it with a parchment-tone hairline border.
- **Soft lift.** The single soft shadow sits on the video play control.

If you add a new floating layer (menu, popover, modal), reuse the layered panel shadow. Do not invent darker or tighter shadows, and do not put shadows on in-flow cards. There is no backdrop blur: headers are opaque `surface` or `surface-alt`.

## Shapes

### Border Radius Scale

| Token        | Value | Use                                                                                                                                                |
| ------------ | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rounded.xs` | 6px   | Compact ghost button (`button-ghost-4`)                                                                                                            |
| `rounded.sm` | 8px   | Standard buttons: `button-primary-3`, `button-secondary`, `button-ghost-2`, `button-secondary-3`. Also the ink chip inside `card` (`card-group-7`) |
| `rounded.md` | 12px  | Text inputs (`input`)                                                                                                                              |
| `rounded.lg` | 16px  | Feature cards (`card-group`), the nav dropdown panel (`header-inner-2-group-4`), the video play control (`video-group`)                            |
| `rounded.xl` | 24px  | Large media such as the hero image and big release surfaces                                                                                        |

The geometry is soft but disciplined.

- **Radius scales with object size.** Small controls get 6–8px, fields 12px, cards and panels 16px, full-width media 24px. Never put a large radius on a small control or a small radius on a hero image.
- **No pills or circles.** Buttons are rounded rectangles, not capsules; avatars and icons are not circle-cropped. Don't introduce `9999px` shapes.
- **Structure stays rectilinear.** Lists and tables are square-edged rows defined by 1px rules. Rounding belongs to objects, not to layout.

## Components

Each component below was distilled from the live page: the recipe is a standalone, placeholder-filled reproduction with literal values, and every frontmatter key named in the anatomy carries the same measurements. A verified component reproduced the original in every check; a flagged one is shipped with the reason it did not; one marked not verifiable could not be compared with the original, which says nothing about the recipe.

### Button, primary

**Verification**: flagged, the render matched 59% of the original pixels, below the 97% required on hover after 2 correction attempts.

**Anatomy**

- `button-primary`: the component root, a `<div>` (`.c-button-primary`)
- `button-primary-group`: inner flex row (`.c-button-primary__group`)
- `button-primary-label`: label text, 23 characters (`.c-button-primary__label`)
- `button-primary-group-2`: inner flex row (`.c-button-primary__group-2`)
- `button-primary-group-3`: inner flex row (`.c-button-primary__group-3`)
- `button-primary-group-4`: inner flex column (`.c-button-primary__group-4`), content not captured

**Recipe**

```html
<div class="c-button-primary-scope">
  <div class="c-button-primary">
    <div class="c-button-primary__group">
      <div class="c-button-primary__label">lorem ipsum dolor sit a</div>
      <div class="c-button-primary__group-2">
        <div class="c-button-primary__group-3">
          <div class="c-button-primary__group-4"></div>
        </div>
      </div>
    </div>
  </div>
</div>
```

```css
.c-button-primary-scope {
  background-color: #f0eee6;
  color: #141413;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
}

.c-button-primary {
  display: flex;
  align-items: center;
  flex-grow: 1;
  flex-basis: 0%;
  column-gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  vertical-align: top;
  color: #141413;
  cursor: pointer;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
  text-decoration-line: underline;
  text-decoration-color: transparent;
  text-align: left;
  white-space: nowrap;
  list-style-type: none;
  transition: text-decoration-color 0.2s ease;
}

.c-button-primary__group {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  width: 45px;
  min-height: 36px;
  position: relative;
  vertical-align: middle;
  background-color: #141413;
  color: #faf9f5;
  font-family: "Anthropic Sans", Arial, sans-serif;
  font-size: 16px;
  line-height: 16px;
  letter-spacing: -0.08px;
  text-align: center;
  border-top: 1px solid #141413;
  border-right: 1px solid #141413;
  border-bottom: 1px solid #141413;
  border-left: 1px solid #3d3d3a;
  border-top-right-radius: 8px;
  border-bottom-right-radius: 8px;
  transition-duration: 0.2s, 0.2s, 0.2s;
  transition-timing-function: ease, ease, ease;
  transition-property: border-color, color, background-color;
}

.c-button-primary__label {
  display: block;
  box-sizing: border-box;
  width: 1px;
  height: 1px;
  position: absolute;
  top: 0%;
  right: 0%;
  left: 0%;
  overflow-x: hidden;
  overflow-y: hidden;
  margin-right: auto;
  margin-left: auto;
}

.c-button-primary__group-2 {
  display: flex;
  align-items: center;
  box-sizing: border-box;
  height: 100%;
}

.c-button-primary__group-3 {
  display: flex;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease;
  margin-left: auto;
}

.c-button-primary__group-4 {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  width: 24px;
  height: 24px;
}

.c-button-primary__group-4::before {
  content: "";
  display: table;
  box-sizing: border-box;
}

.c-button-primary__group-4::after {
  content: "";
  display: table;
  box-sizing: border-box;
}

.c-button-primary:hover {
  text-decoration-color: #141413;
}

.c-button-primary:focus {
  outline: 2px solid #141413;
  outline-offset: -2px;
}
```

**States**

- hover: text-decoration-color #141413
- focus: outline 2px solid #141413, outline-offset -2px

### Button, ghost

**Verification**: verified against the live page at desktop.

**Anatomy**

- `button-ghost`: the component root, a `<button>` (`.c-button-ghost`), 15-character label

**Recipe**

```html
<div class="c-button-ghost-scope">
  <button class="c-button-ghost" type="button">lorem ipsum dol</button>
</div>
```

```css
.c-button-ghost-scope {
  background-color: #141413;
  color: #faf9f5;
  font-family: "Anthropic Sans", Arial, sans-serif;
  font-size: 12px;
  font-weight: 400;
  line-height: 16.8px;
}

.c-button-ghost {
  display: inline-block;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #b0aea5;
  border: 0;
  cursor: pointer;
  font-family: "Anthropic Sans", Arial, sans-serif;
  font-size: 12px;
  font-weight: 400;
  line-height: 16.8px;
  letter-spacing: -0.24px;
  text-transform: none;
  text-align: start;
  list-style-type: none;
  appearance: button;
}

.c-button-ghost:hover {
  color: #faf9f5;
  text-decoration-line: underline;
  text-decoration-color: #faf9f5;
}

.c-button-ghost:focus {
  outline: 2px solid #faf9f5;
  outline-offset: 4px;
}
```

**States**

- hover (`button-ghost-hover`): color #FAF9F5, text-decoration-line underline, text-decoration-color #FAF9F5
- focus: outline 2px solid #FAF9F5, outline-offset 4px

### Card

**Verification**: flagged, the `card-group` height did not reproduce the measured 559px after 2 correction attempts.

**Anatomy**

- Group: 3 instances in a 3-column grid, 31.4776px gap; the recipe carries the values they all share
- `card`: the component root, a `<div>` (`.c-card`)
- `card-group`: inner flex row (`.c-card__group`)
- `card-group-2`: inner block (`.c-card__group-2`)
- `card-group-3`: inner flex column (`.c-card__group-3`)
- `card-group-4`: inner block (`.c-card__group-4`)
- `card-title`: heading, 22 characters (`.c-card__title`)
- `card-body`: label text, 90 characters (`.c-card__body`), content not captured
- `card-group-5`: inner block (`.c-card__group-5`)
- `card-group-6`: inner block (`.c-card__group-6`)
- `card-list`: inner group (`.c-card__list`), content not captured
- `card-group-7`: inner flex row (`.c-card__group-7`), content not captured

**Recipe**

```html
<div class="c-card-scope">
  <div class="c-card">
    <div class="c-card__group">
      <div class="c-card__group-2"></div>
      <div class="c-card__group-3">
        <div class="c-card__group-4">
          <h3 class="c-card__title">lorem ipsum dolor sit</h3>
          <p class="c-card__body">
            lorem ipsum dolor sit amet consectetur adipiscing elit sed do
            eiusmod tempor lorem ipsum d
          </p>
        </div>
        <div class="c-card__group-5"></div>
        <div class="c-card__group-6">
          <ul class="c-card__list"></ul>
          <div class="c-card__group-7"></div>
        </div>
      </div>
    </div>
  </div>
</div>
```

```css
.c-card-scope {
  background-color: #f0eee6;
  color: #141413;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
}

.c-card {
  display: inline-block;
  border-spacing: 0px;
  box-sizing: border-box;
  color: #141413;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
}

.c-card__group {
  display: flex;
  justify-content: space-between;
  gap: 31.4776px;
  box-sizing: border-box;
  height: 100%;
  padding: 31.4776px;
  position: relative;
  overflow-x: hidden;
  overflow-y: hidden;
  border-radius: 16px;
}

.c-card__group-2 {
  display: block;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0%;
  right: 0%;
  bottom: 0%;
  left: 0%;
  background-color: #e3dacc;
}

.c-card__group-3 {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-grow: 1;
  flex-basis: 0%;
  box-sizing: border-box;
  position: relative;
  z-index: 1;
}

.c-card__group-4 {
  display: block;
  box-sizing: border-box;
  max-width: 432.245px;
}

.c-card__title {
  display: flow-root;
  box-sizing: border-box;
  margin: 0px 0px 16px;
  font-family: "Anthropic Sans", Arial, sans-serif;
  font-size: 24px;
  font-weight: 600;
  line-height: 31.2px;
}

.c-card__title::before {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -7.43375px;
}

.c-card__title::after {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -5.99375px;
}

.c-card__body {
  display: flow-root;
  box-sizing: border-box;
  margin: 0px 0px 16px;
  font-size: 18px;
  line-height: 25.2px;
}

.c-card__body::before {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -4.67375px;
}

.c-card__body::after {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -7.73375px;
}

.c-card__group-5 {
  display: block;
  box-sizing: border-box;
  height: 90.7755px;
}

.c-card__group-6 {
  display: block;
  box-sizing: border-box;
}

.c-card__list {
  display: block;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px 0px 31.4776px;
  list-style-type: none;
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: #1414131a;
}

.c-card__group-7 {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  min-height: 36px;
  padding: 8px 16px;
  position: relative;
  vertical-align: middle;
  background-color: #141413;
  color: #faf9f5;
  border: 1px solid #141413;
  border-radius: 8px;
  font-family: "Anthropic Sans", Arial, sans-serif;
  font-size: 16px;
  line-height: 16px;
  letter-spacing: -0.08px;
  text-align: center;
  transition-duration: 0.2s, 0.2s, 0.2s;
  transition-timing-function: ease, ease, ease;
  transition-property: border-color, color, background-color;
}
```

**States**

- No hover or focus change was observed.

### Nav menu

**Verification**: flagged, the `nav-menu-group-2` x did not reproduce the measured 495px after 2 correction attempts.

**Anatomy**

- `nav-menu`: the component root, a `<nav>` (`.c-nav-menu`)
- `nav-menu-group`: inner flex row (`.c-nav-menu__group`)
- `nav-menu-list`: inner flex row (`.c-nav-menu__list`)
- `nav-menu-group-2`: inner block (`.c-nav-menu__group-2`, 3 instances), content not captured
- `nav-menu-link`: link (`.c-nav-menu__link`, 2 instances), content not captured
- `nav-menu-group-3`: inner flex row (`.c-nav-menu__group-3`), content not captured

**Recipe**

```html
<div class="c-nav-menu-scope">
  <nav class="c-nav-menu">
    <div class="c-nav-menu__group">
      <ul class="c-nav-menu__list">
        <div class="c-nav-menu__group-2"></div>
        <a class="c-nav-menu__link" href="#"></a>
        <div class="c-nav-menu__group-2"></div>
        <div class="c-nav-menu__group-2"></div>
        <a class="c-nav-menu__link" href="#"></a>
        <div class="c-nav-menu__group-3"></div>
      </ul>
    </div>
  </nav>
</div>
```

```css
.c-nav-menu-scope {
  background-color: #f0eee6;
  color: #141413;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
}

.c-nav-menu {
  display: inline-flex;
  flex-grow: 1;
  flex-basis: 0%;
  border-spacing: 0px;
  box-sizing: border-box;
  color: #141413;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
}

.c-nav-menu__group {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  flex-grow: 1;
  flex-basis: 0%;
  column-gap: 28px;
  box-sizing: border-box;
}

.c-nav-menu__list {
  display: flex;
  justify-content: flex-end;
  flex-grow: 1;
  flex-basis: 0%;
  box-sizing: border-box;
  width: 100%;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-nav-menu__group-2 {
  display: inline-block;
  box-sizing: border-box;
  width: 100%;
  text-align: left;
}

.c-nav-menu__link {
  display: flex;
  align-items: center;
  flex-grow: 1;
  flex-basis: 0%;
  column-gap: 8px;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  max-width: 100%;
  padding: 22.4px 12px;
  color: #141413;
  cursor: pointer;
  text-decoration-line: underline;
  text-decoration-color: transparent;
  transition: text-decoration-color 0.2s ease;
}

.c-nav-menu__group-3 {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  height: 100%;
  padding-left: 12px;
}
```

**States**

- No hover or focus change was observed.

### Nav menu (2)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `nav-menu-2`: the component root, a `<nav>` (`.c-nav-menu-2`)
- `nav-menu-2-group`: inner flex column (`.c-nav-menu-2__group`)
- `nav-menu-2-icon`: icon placeholder, 45x32px (`.c-nav-menu-2__icon`)
- `nav-menu-2-group-2`: inner flex column (`.c-nav-menu-2__group-2`)
- `nav-menu-2-text`: label text, 0 characters (`.c-nav-menu-2__text`)
- `nav-menu-2-text-2`: label text, 1 characters (`.c-nav-menu-2__text-2`, 3 instances)
- `nav-menu-2-list`: inner flex row (`.c-nav-menu-2__list`)
- `nav-menu-2-item`: inner flex row (`.c-nav-menu-2__item`, 3 instances), content not captured
- `nav-menu-2-group-3`: inner grid (`.c-nav-menu-2__group-3`)
- `nav-menu-2-group-4`: inner flex column (`.c-nav-menu-2__group-4`, 4 instances), content not captured
- `nav-menu-2-group-5`: inner block (`.c-nav-menu-2__group-5`, 8 instances)
- `nav-menu-2-title`: heading, 8 characters (`.c-nav-menu-2__title`, 8 instances)
- `nav-menu-2-list-2`: inner flex column (`.c-nav-menu-2__list-2`, 8 instances), content not captured

**Recipe**

```html
<div class="c-nav-menu-2-scope">
  <nav class="c-nav-menu-2">
    <div class="c-nav-menu-2__group">
      <span class="c-nav-menu-2__icon" aria-hidden="true"></span>
      <div class="c-nav-menu-2__group-2">
        <div class="c-nav-menu-2__text">
          <span class="c-nav-menu-2__text-2">l</span>
          <span class="c-nav-menu-2__text-2">lore</span>
          <span class="c-nav-menu-2__text-2"
            >lorem ipsum dolor sit amet consectetur adipiscing elit sed do
            eiusmod tempor</span
          >
        </div>
        <ul class="c-nav-menu-2__list">
          <li class="c-nav-menu-2__item"></li>
          <li class="c-nav-menu-2__item"></li>
          <li class="c-nav-menu-2__item"></li>
        </ul>
      </div>
    </div>
    <div class="c-nav-menu-2__group-3">
      <section class="c-nav-menu-2__group-4">
        <div class="c-nav-menu-2__group-5">
          <h3 class="c-nav-menu-2__title">lorem ip</h3>
          <ul class="c-nav-menu-2__list-2"></ul>
        </div>
        <div class="c-nav-menu-2__group-5">
          <h3 class="c-nav-menu-2__title">lorem</h3>
          <ul class="c-nav-menu-2__list-2"></ul>
        </div>
      </section>
      <section class="c-nav-menu-2__group-4">
        <div class="c-nav-menu-2__group-5">
          <h3 class="c-nav-menu-2__title">lorem ips</h3>
          <ul class="c-nav-menu-2__list-2"></ul>
        </div>
        <div class="c-nav-menu-2__group-5">
          <h3 class="c-nav-menu-2__title">lorem ipsum dol</h3>
          <ul class="c-nav-menu-2__list-2"></ul>
        </div>
      </section>
      <section class="c-nav-menu-2__group-4">
        <div class="c-nav-menu-2__group-5">
          <h3 class="c-nav-menu-2__title">lorem ips</h3>
          <ul class="c-nav-menu-2__list-2"></ul>
        </div>
        <div class="c-nav-menu-2__group-5">
          <h3 class="c-nav-menu-2__title">lorem ip</h3>
          <ul class="c-nav-menu-2__list-2"></ul>
        </div>
        <div class="c-nav-menu-2__group-5">
          <h3 class="c-nav-menu-2__title">lorem ipsum dolor</h3>
          <ul class="c-nav-menu-2__list-2"></ul>
        </div>
      </section>
      <section class="c-nav-menu-2__group-4">
        <div class="c-nav-menu-2__group-5">
          <h3 class="c-nav-menu-2__title">lorem i</h3>
          <ul class="c-nav-menu-2__list-2"></ul>
        </div>
      </section>
    </div>
  </nav>
</div>
```

```css
.c-nav-menu-2-scope {
  background-color: #141413;
  color: #faf9f5;
  font-family: "Anthropic Sans", Arial, sans-serif;
  font-size: 12px;
  font-weight: 400;
  line-height: 16.8px;
}

.c-nav-menu-2 {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 31.4776px;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
  grid-template-rows: auto;
  border-spacing: 0px;
  box-sizing: border-box;
  color: #faf9f5;
  font-family: "Anthropic Sans", Arial, sans-serif;
  font-size: 12px;
  font-weight: 400;
  line-height: 16.8px;
}

.c-nav-menu-2__group {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-sizing: border-box;
  width: 297.527px;
}

.c-nav-menu-2__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 45px;
  height: 32px;
  max-width: 100%;
  overflow-x: hidden;
  overflow-y: hidden;
  background-color: currentcolor;
}

.c-nav-menu-2__group-2 {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;
  gap: 12px;
  box-sizing: border-box;
  width: 100%;
}

.c-nav-menu-2__text {
  display: block;
  box-sizing: border-box;
  color: #b0aea5;
}

.c-nav-menu-2__list {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: "";
}

.c-nav-menu-2__item {
  display: flex;
  box-sizing: border-box;
}

.c-nav-menu-2__group-3 {
  display: grid;
  justify-content: space-between;
  flex-grow: 1;
  flex-basis: 0%;
  gap: 31.4776px;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: auto;
  box-sizing: border-box;
}

.c-nav-menu-2__group-4 {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  flex-basis: 0%;
  gap: 46.4327px;
  box-sizing: border-box;
  position: relative;
}

.c-nav-menu-2__group-5 {
  display: block;
  box-sizing: border-box;
}

.c-nav-menu-2__title {
  display: flow-root;
  box-sizing: border-box;
  margin: 0px 0px 8px;
  font-size: 12px;
  font-weight: 500;
}

.c-nav-menu-2__title::before {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -4.31844px;
}

.c-nav-menu-2__title::after {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -3.59844px;
}

.c-nav-menu-2__list-2 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}
```

**States**

- No hover or focus change was observed.

### Hero

**Verification**: flagged, the `hero-group-4` x did not reproduce the measured 845px after 2 correction attempts.

**Anatomy**

- `hero`: the component root, a `<header>` (`.c-hero`)
- `hero-group`: inner block (`.c-hero__group`)
- `hero-group-2`: inner block (`.c-hero__group-2`)
- `hero-group-3`: inner grid (`.c-hero__group-3`)
- `hero-title`: heading, 0 characters (`.c-hero__title`), content not captured
- `hero-group-4`: inner block (`.c-hero__group-4`), content not captured
- `hero-group-5`: inner block (`.c-hero__group-5`)

**Recipe**

```html
<div class="c-hero-scope">
  <header class="c-hero">
    <div class="c-hero__group"></div>
    <div class="c-hero__group-2">
      <div class="c-hero__group-3">
        <h1 class="c-hero__title"></h1>
        <div class="c-hero__group-4"></div>
      </div>
    </div>
    <div class="c-hero__group-5"></div>
  </header>
</div>
```

```css
.c-hero-scope {
  background-color: #f0eee6;
  color: #141413;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
}

.c-hero {
  display: inline-flex;
  flex-direction: column;
  border-spacing: 0px;
  box-sizing: border-box;
  position: relative;
  color: #141413;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
  text-align: left;
}

.c-hero__group {
  display: block;
  box-sizing: border-box;
  height: 150.596px;
}

.c-hero__group-2 {
  display: block;
  box-sizing: border-box;
  width: 100%;
  max-width: 1284.54px;
  position: relative;
  margin-right: auto;
  margin-left: auto;
}

.c-hero__group-3 {
  display: grid;
  align-items: end;
  gap: 31.4776px;
  grid-template-columns: repeat(12, minmax(0px, 1fr));
  grid-template-rows: auto;
  box-sizing: border-box;
}

.c-hero__title {
  display: flow-root;
  box-sizing: border-box;
  margin: 0px;
  font-family: "Anthropic Sans", Arial, sans-serif;
  font-size: 60.8653px;
  font-weight: 700;
  line-height: 66.9518px;
}

.c-hero__title::before {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -12.7745px;
}

.c-hero__title::after {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -9.12263px;
}

.c-hero__group-4 {
  display: block;
  box-sizing: border-box;
  padding-bottom: 5px;
}

.c-hero__group-5 {
  display: block;
  box-sizing: border-box;
  height: 60.8653px;
}
```

**States**

- No hover or focus change was observed.

### Nav dropdown

**Verification**: flagged, the render matched 91% of the original pixels, below the 96% required on focus after 2 correction attempts.

**Anatomy**

- `nav-dropdown`: the component root, a `<div>` (`.c-nav-dropdown`)
- `nav-dropdown-text`: label text, 8 characters (`.c-nav-dropdown__text`)
- `nav-dropdown-group`: inner flex row (`.c-nav-dropdown__group`)
- `nav-dropdown-group-2`: inner flex column (`.c-nav-dropdown__group-2`)
- `nav-dropdown-icon`: icon placeholder, 12x24px (`.c-nav-dropdown__icon`)

**Recipe**

```html
<div class="c-nav-dropdown-scope">
  <div class="c-nav-dropdown">
    <div class="c-nav-dropdown__text">lorem ip</div>
    <div class="c-nav-dropdown__group">
      <div class="c-nav-dropdown__group-2">
        <span class="c-nav-dropdown__icon" aria-hidden="true"></span>
      </div>
    </div>
  </div>
</div>
```

```css
.c-nav-dropdown-scope {
  background-color: #f0eee6;
  color: #141413;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
}

.c-nav-dropdown {
  display: flex;
  align-items: center;
  flex-grow: 1;
  flex-basis: 0%;
  column-gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 22.4px 12px;
  vertical-align: top;
  color: #141413;
  cursor: pointer;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
  text-decoration-line: underline;
  text-decoration-color: transparent;
  text-align: left;
  white-space: nowrap;
  list-style-type: none;
  transition: text-decoration-color 0.2s ease;
}

.c-nav-dropdown__text {
  display: block;
  box-sizing: border-box;
  font-family: "Anthropic Sans", Arial, sans-serif;
  font-size: 15px;
  line-height: 21px;
  letter-spacing: -0.0375px;
}

.c-nav-dropdown__group {
  display: flex;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease;
  margin-left: auto;
}

.c-nav-dropdown__group-2 {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  width: 24px;
  height: 24px;
}

.c-nav-dropdown__group-2::before {
  content: "";
  display: table;
  box-sizing: border-box;
}

.c-nav-dropdown__group-2::after {
  content: "";
  display: table;
  box-sizing: border-box;
}

.c-nav-dropdown__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 24px;
  max-width: 100%;
  overflow-x: hidden;
  overflow-y: hidden;
  background-color: currentcolor;
}

.c-nav-dropdown:hover {
  text-decoration-color: #141413;
}

.c-nav-dropdown:focus {
  outline: 2px solid #141413;
  outline-offset: -2px;
}
```

**States**

- hover: text-decoration-color #141413
- focus: outline 2px solid #141413, outline-offset -2px

### Nav dropdown (2)

**Verification**: flagged, the render matched 91% of the original pixels, below the 96% required on focus after 2 correction attempts.

**Anatomy**

- `nav-dropdown-2`: the component root, a `<div>` (`.c-nav-dropdown-2`)
- `nav-dropdown-2-text`: label text, 11 characters (`.c-nav-dropdown-2__text`)
- `nav-dropdown-2-group`: inner flex row (`.c-nav-dropdown-2__group`)
- `nav-dropdown-2-group-2`: inner flex column (`.c-nav-dropdown-2__group-2`)
- `nav-dropdown-2-icon`: icon placeholder, 12x24px (`.c-nav-dropdown-2__icon`)

**Recipe**

```html
<div class="c-nav-dropdown-2-scope">
  <div class="c-nav-dropdown-2">
    <div class="c-nav-dropdown-2__text">lorem ipsum</div>
    <div class="c-nav-dropdown-2__group">
      <div class="c-nav-dropdown-2__group-2">
        <span class="c-nav-dropdown-2__icon" aria-hidden="true"></span>
      </div>
    </div>
  </div>
</div>
```

```css
.c-nav-dropdown-2-scope {
  background-color: #f0eee6;
  color: #141413;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
}

.c-nav-dropdown-2 {
  display: flex;
  align-items: center;
  flex-grow: 1;
  flex-basis: 0%;
  column-gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 22.4px 12px;
  vertical-align: top;
  color: #141413;
  cursor: pointer;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
  text-decoration-line: underline;
  text-decoration-color: transparent;
  text-align: left;
  white-space: nowrap;
  list-style-type: none;
  transition: text-decoration-color 0.2s ease;
}

.c-nav-dropdown-2__text {
  display: block;
  box-sizing: border-box;
  font-family: "Anthropic Sans", Arial, sans-serif;
  font-size: 15px;
  line-height: 21px;
  letter-spacing: -0.0375px;
}

.c-nav-dropdown-2__group {
  display: flex;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease;
  margin-left: auto;
}

.c-nav-dropdown-2__group-2 {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  width: 24px;
  height: 24px;
}

.c-nav-dropdown-2__group-2::before {
  content: "";
  display: table;
  box-sizing: border-box;
}

.c-nav-dropdown-2__group-2::after {
  content: "";
  display: table;
  box-sizing: border-box;
}

.c-nav-dropdown-2__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 24px;
  max-width: 100%;
  overflow-x: hidden;
  overflow-y: hidden;
  background-color: currentcolor;
}

.c-nav-dropdown-2:hover {
  text-decoration-color: #141413;
}

.c-nav-dropdown-2:focus {
  outline: 2px solid #141413;
  outline-offset: -2px;
}
```

**States**

- hover: text-decoration-color #141413
- focus: outline 2px solid #141413, outline-offset -2px

### Nav dropdown (3)

**Verification**: flagged, the render matched 90% of the original pixels, below the 96% required on focus after 2 correction attempts.

**Anatomy**

- `nav-dropdown-3`: the component root, a `<div>` (`.c-nav-dropdown-3`)
- `nav-dropdown-3-text`: label text, 5 characters (`.c-nav-dropdown-3__text`)
- `nav-dropdown-3-group`: inner flex row (`.c-nav-dropdown-3__group`)
- `nav-dropdown-3-group-2`: inner flex column (`.c-nav-dropdown-3__group-2`)
- `nav-dropdown-3-icon`: icon placeholder, 12x24px (`.c-nav-dropdown-3__icon`)

**Recipe**

```html
<div class="c-nav-dropdown-3-scope">
  <div class="c-nav-dropdown-3">
    <div class="c-nav-dropdown-3__text">lorem</div>
    <div class="c-nav-dropdown-3__group">
      <div class="c-nav-dropdown-3__group-2">
        <span class="c-nav-dropdown-3__icon" aria-hidden="true"></span>
      </div>
    </div>
  </div>
</div>
```

```css
.c-nav-dropdown-3-scope {
  background-color: #f0eee6;
  color: #141413;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
}

.c-nav-dropdown-3 {
  display: flex;
  align-items: center;
  flex-grow: 1;
  flex-basis: 0%;
  column-gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 22.4px 12px;
  vertical-align: top;
  color: #141413;
  cursor: pointer;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
  text-decoration-line: underline;
  text-decoration-color: transparent;
  text-align: left;
  white-space: nowrap;
  list-style-type: none;
  transition: text-decoration-color 0.2s ease;
}

.c-nav-dropdown-3__text {
  display: block;
  box-sizing: border-box;
  font-family: "Anthropic Sans", Arial, sans-serif;
  font-size: 15px;
  line-height: 21px;
  letter-spacing: -0.0375px;
}

.c-nav-dropdown-3__group {
  display: flex;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease;
  margin-left: auto;
}

.c-nav-dropdown-3__group-2 {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  width: 24px;
  height: 24px;
}

.c-nav-dropdown-3__group-2::before {
  content: "";
  display: table;
  box-sizing: border-box;
}

.c-nav-dropdown-3__group-2::after {
  content: "";
  display: table;
  box-sizing: border-box;
}

.c-nav-dropdown-3__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 24px;
  max-width: 100%;
  overflow-x: hidden;
  overflow-y: hidden;
  background-color: currentcolor;
}

.c-nav-dropdown-3:hover {
  text-decoration-color: #141413;
}

.c-nav-dropdown-3:focus {
  outline: 2px solid #141413;
  outline-offset: -2px;
}
```

**States**

- hover: text-decoration-color #141413
- focus: outline 2px solid #141413, outline-offset -2px

### Header (landing)

**Verification**: flagged, the `header-landing-nav-link` height did not reproduce the measured 69px after 2 correction attempts.

Variant observed on https://www.anthropic.com/.

**Anatomy**

- `header-landing`: the component root, a `<div>` (`.c-header-landing`)
- `header-landing-inner`: inner flex row (`.c-header-landing__inner`)
- `header-landing-logo`: link (`.c-header-landing__logo`)
- `header-landing-group`: inner flex row (`.c-header-landing__group`)
- `header-landing-logo-icon`: icon placeholder, 143x16px (`.c-header-landing__logo-icon`)
- `header-landing-nav`: inner flex row (`.c-header-landing__nav`)
- `header-landing-group-2`: inner flex row (`.c-header-landing__group-2`)
- `header-landing-nav-list`: inner flex row (`.c-header-landing__nav-list`)
- `header-landing-group-3`: inner flex row (`.c-header-landing__group-3`, 3 instances)
- `header-landing-text`: label text, 8 characters (`.c-header-landing__text`, 5 instances)
- `header-landing-group-4`: inner flex row (`.c-header-landing__group-4`, 3 instances), content not captured
- `header-landing-nav-item`: inner group (`.c-header-landing__nav-item`)
- `header-landing-nav-link`: link (`.c-header-landing__nav-link`, 2 instances)
- `header-landing-group-5`: inner flex row (`.c-header-landing__group-5`)
- `header-landing-group-6`: inner flex row (`.c-header-landing__group-6`)
- `header-landing-group-7`: inner block (`.c-header-landing__group-7`), content not captured
- `header-landing-text-2`: label text, 10 characters (`.c-header-landing__text-2`)
- `header-landing-group-8`: inner block (`.c-header-landing__group-8`)
- `header-landing-cta`: inner flex row (`.c-header-landing__cta`), content not captured

**Recipe**

```html
<div class="c-header-landing-scope">
  <div class="c-header-landing">
    <div class="c-header-landing__inner">
      <a class="c-header-landing__logo" href="#">
        <div class="c-header-landing__group">
          <span class="c-header-landing__logo-icon" aria-hidden="true"></span>
        </div>
      </a>
      <nav class="c-header-landing__nav">
        <div class="c-header-landing__group-2">
          <ul class="c-header-landing__nav-list">
            <div class="c-header-landing__group-3">
              <div class="c-header-landing__text">lorem ip</div>
              <div class="c-header-landing__group-4"></div>
            </div>
            <li class="c-header-landing__nav-item">
              <a class="c-header-landing__nav-link" href="#">
                <div class="c-header-landing__text">lorem</div>
              </a>
            </li>
            <div class="c-header-landing__group-3">
              <div class="c-header-landing__text">lorem ipsum</div>
              <div class="c-header-landing__group-4"></div>
            </div>
            <div class="c-header-landing__group-3">
              <div class="c-header-landing__text">lorem</div>
              <div class="c-header-landing__group-4"></div>
            </div>
            <a class="c-header-landing__nav-link" href="#">
              <div class="c-header-landing__text">lore</div>
            </a>
            <div class="c-header-landing__group-5">
              <div class="c-header-landing__group-6">
                <div class="c-header-landing__group-7"></div>
                <div class="c-header-landing__text-2">lorem ipsu</div>
              </div>
              <div class="c-header-landing__group-8">
                <div class="c-header-landing__cta"></div>
              </div>
            </div>
          </ul>
        </div>
      </nav>
    </div>
  </div>
</div>
```

```css
.c-header-landing-scope {
  background-color: #f0eee6;
  color: #141413;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
}

.c-header-landing {
  display: block;
  border-spacing: 0px;
  box-sizing: border-box;
  position: relative;
  z-index: 1;
  background-color: #f0eee6;
  color: #141413;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
}

.c-header-landing__inner {
  display: flex;
  justify-content: space-between;
  column-gap: 12px;
  box-sizing: border-box;
  width: 100%;
  height: 68px;
  max-width: 1284.54px;
  margin-right: auto;
  margin-left: auto;
}

.c-header-landing__logo {
  display: flex;
  align-items: center;
  box-sizing: border-box;
  width: 144px;
  max-width: 100%;
  position: relative;
  z-index: 2;
  color: #141413;
  cursor: pointer;
  text-decoration-line: none;
  transition: color 0.2s ease;
}

.c-header-landing__group {
  display: flex;
  box-sizing: border-box;
  height: 16px;
}

.c-header-landing__logo-icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 143px;
  height: 16px;
  max-width: 100%;
  overflow-x: hidden;
  overflow-y: hidden;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 0);
}

.c-header-landing__nav {
  display: flex;
  flex-grow: 1;
  flex-basis: 0%;
  box-sizing: border-box;
}

.c-header-landing__group-2 {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  flex-grow: 1;
  flex-basis: 0%;
  column-gap: 28px;
  box-sizing: border-box;
}

.c-header-landing__nav-list {
  display: flex;
  justify-content: flex-end;
  flex-grow: 1;
  flex-basis: 0%;
  box-sizing: border-box;
  width: 100%;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-header-landing__group-3 {
  display: flex;
  align-items: center;
  flex-grow: 1;
  flex-basis: 0%;
  column-gap: 8px;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  padding: 22.4px 12px;
  vertical-align: top;
  cursor: pointer;
  text-decoration-line: underline;
  text-decoration-color: transparent;
  text-align: left;
  white-space: nowrap;
  transition: text-decoration-color 0.2s ease;
  margin-right: auto;
  margin-left: auto;
}

.c-header-landing__text {
  display: block;
  box-sizing: border-box;
  font-family: "Anthropic Sans", Arial, sans-serif;
  font-size: 15px;
  line-height: 21px;
  letter-spacing: -0.0375px;
}

.c-header-landing__group-4 {
  display: flex;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease;
  margin-left: auto;
}

.c-header-landing__nav-item {
  display: block;
  box-sizing: border-box;
}

.c-header-landing__nav-link {
  display: flex;
  align-items: center;
  flex-grow: 1;
  flex-basis: 0%;
  column-gap: 8px;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  max-width: 100%;
  padding: 22.4px 12px;
  color: #141413;
  cursor: pointer;
  text-decoration-line: underline;
  text-decoration-color: transparent;
  transition: text-decoration-color 0.2s ease;
}

.c-header-landing__group-5 {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  height: 100%;
  padding-left: 12px;
}

.c-header-landing__group-6 {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  min-height: 36px;
  padding: 8px 16px;
  position: relative;
  vertical-align: middle;
  background-color: #141413;
  color: #faf9f5;
  border: 1px solid #141413;
  font-family: "Anthropic Sans", Arial, sans-serif;
  font-size: 16px;
  line-height: 16px;
  letter-spacing: -0.08px;
  text-align: center;
  white-space: nowrap;
  border-top-left-radius: 8px;
  border-bottom-left-radius: 8px;
  transition-duration: 0.2s, 0.2s, 0.2s;
  transition-timing-function: ease, ease, ease;
  transition-property: border-color, color, background-color;
}

.c-header-landing__group-7 {
  display: block;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0%;
  right: 0%;
  bottom: 0%;
  left: 0%;
  z-index: 3;
  cursor: pointer;
  border-top-left-radius: 8px;
  border-bottom-left-radius: 8px;
}

.c-header-landing__text-2 {
  display: block;
  box-sizing: border-box;
  position: relative;
  z-index: 2;
  font-size: 15px;
  line-height: 15px;
}

.c-header-landing__group-8 {
  display: block;
  box-sizing: border-box;
  width: 100%;
  position: relative;
  text-align: left;
}

.c-header-landing__cta {
  display: flex;
  align-items: center;
  flex-grow: 1;
  flex-basis: 0%;
  column-gap: 8px;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  vertical-align: top;
  cursor: pointer;
  text-decoration-line: underline;
  text-decoration-color: transparent;
  white-space: nowrap;
  transition: text-decoration-color 0.2s ease;
  margin-right: auto;
  margin-left: auto;
}

.c-header-landing__logo:hover {
  color: #5e5d59;
}

.c-header-landing__logo:focus {
  outline: 2px solid #141413;
  outline-offset: -2px;
}

.c-header-landing__nav-link:hover {
  text-decoration-color: #141413;
}

.c-header-landing__nav-link:focus {
  outline: 2px solid #141413;
  outline-offset: -2px;
}
```

**States**

- `header-landing-logo` hover (`header-landing-logo-hover`): color #5E5D59
- `header-landing-logo` focus: outline 2px solid #141413, outline-offset -2px
- `header-landing-nav-link` hover: text-decoration-color #141413
- `header-landing-nav-link` focus: outline 2px solid #141413, outline-offset -2px

### Footer (landing)

**Verification**: desktop flagged, the `footer-landing-inner` height did not reproduce the measured 981px after 2 correction attempts; mobile flagged, the `footer-landing-mobile-inner` height did not reproduce the measured 3188px after 2 correction attempts.

Variant observed on https://www.anthropic.com/.

**Anatomy**

- `footer-landing`: the component root, a `<footer>` (`.c-footer-landing`)
- `footer-landing-heading`: heading, 6 characters (`.c-footer-landing__heading`)
- `footer-landing-inner`: inner block (`.c-footer-landing__inner`)
- `footer-landing-nav`: inner flex row (`.c-footer-landing__nav`)
- `footer-landing-group`: inner flex column (`.c-footer-landing__group`)
- `footer-landing-icon`: icon placeholder, 45x32px (`.c-footer-landing__icon`)
- `footer-landing-group-2`: inner flex column (`.c-footer-landing__group-2`)
- `footer-landing-group-3`: inner block (`.c-footer-landing__group-3`)
- `footer-landing-text`: label text, 1 characters (`.c-footer-landing__text`, 2 instances)
- `footer-landing-text-2`: label text, 76 characters (`.c-footer-landing__text-2`)
- `footer-landing-list`: inner flex row (`.c-footer-landing__list`)
- `footer-landing-nav-item`: inner flex row (`.c-footer-landing__nav-item`, 3 instances)
- `footer-landing-nav-link`: link (`.c-footer-landing__nav-link`, 3 instances)
- `footer-landing-group-4`: inner flex row (`.c-footer-landing__group-4`, 3 instances), content not captured
- `footer-landing-columns`: inner grid (`.c-footer-landing__columns`), content not captured
- `footer-landing-column`: inner flex column (`.c-footer-landing__column`, 2 instances)
- `footer-landing-group-5`: inner block (`.c-footer-landing__group-5`, 4 instances)
- `footer-landing-column-heading`: heading, 8 characters (`.c-footer-landing__column-heading`, 4 instances)
- `footer-landing-list-2`: inner flex column (`.c-footer-landing__list-2`, 4 instances), content not captured
- `footer-landing-nav-item-2`: inner flex row (`.c-footer-landing__nav-item-2`, 43 instances), content not captured
- `footer-landing-nav-link-2`: link (`.c-footer-landing__nav-link-2`, 42 instances), content not captured

**Desktop recipe**

```html
<div class="c-footer-landing-scope">
  <footer class="c-footer-landing">
    <h2 class="c-footer-landing__heading">lorem</h2>
    <div class="c-footer-landing__inner">
      <nav class="c-footer-landing__nav">
        <div class="c-footer-landing__group">
          <span class="c-footer-landing__icon" aria-hidden="true"></span>
          <div class="c-footer-landing__group-2">
            <div class="c-footer-landing__group-3">
              <span class="c-footer-landing__text">l</span>
              <span class="c-footer-landing__text">lore</span>
              <span class="c-footer-landing__text-2"
                >lorem ipsum dolor sit amet consectetur adipiscing elit sed do
                eiusmod tempor</span
              >
            </div>
            <ul class="c-footer-landing__list">
              <li class="c-footer-landing__nav-item">
                <a class="c-footer-landing__nav-link" href="#">
                  <div class="c-footer-landing__group-4"></div>
                </a>
              </li>
              <li class="c-footer-landing__nav-item">
                <a class="c-footer-landing__nav-link" href="#">
                  <div class="c-footer-landing__group-4"></div>
                </a>
              </li>
              <li class="c-footer-landing__nav-item">
                <a class="c-footer-landing__nav-link" href="#">
                  <div class="c-footer-landing__group-4"></div>
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div class="c-footer-landing__columns">
          <section class="c-footer-landing__column">
            <div class="c-footer-landing__group-5">
              <h3 class="c-footer-landing__column-heading">lorem ip</h3>
              <ul class="c-footer-landing__list-2">
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
              </ul>
            </div>
            <div class="c-footer-landing__group-5">
              <h3 class="c-footer-landing__column-heading">lorem</h3>
              <ul class="c-footer-landing__list-2">
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
              </ul>
            </div>
          </section>
          <section class="c-footer-landing__column">
            <div class="c-footer-landing__group-5">
              <h3 class="c-footer-landing__column-heading">lorem ips</h3>
              <ul class="c-footer-landing__list-2">
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
              </ul>
            </div>
            <div class="c-footer-landing__group-5">
              <h3 class="c-footer-landing__column-heading">lorem ipsum dol</h3>
              <ul class="c-footer-landing__list-2">
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2">
                  <a class="c-footer-landing__nav-link-2" href="#"></a>
                </li>
                <li class="c-footer-landing__nav-item-2"></li>
              </ul>
            </div>
          </section>
        </div>
      </nav>
    </div>
  </footer>
</div>
```

```css
.c-footer-landing-scope {
  background-color: #f0eee6;
  color: #141413;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
}

.c-footer-landing {
  display: inline-block;
  border-spacing: 0px;
  box-sizing: border-box;
  position: relative;
  background-color: #141413;
  color: #faf9f5;
  font-family: "Anthropic Sans", Arial, sans-serif;
  font-size: 12px;
  font-weight: 400;
  line-height: 16.8px;
}

.c-footer-landing__heading {
  display: flow-root;
  box-sizing: border-box;
  width: 1px;
  height: 1px;
  margin: 0px auto;
  position: absolute;
  top: 0%;
  right: 0%;
  left: 0%;
  overflow-x: hidden;
  overflow-y: hidden;
  font-size: 12px;
  font-weight: 400;
  white-space: nowrap;
}

.c-footer-landing__heading::before {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -4.31844px;
}

.c-footer-landing__heading::after {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -3.59844px;
}

.c-footer-landing__inner {
  display: block;
  box-sizing: border-box;
  width: 100%;
  max-width: 1284.54px;
  position: relative;
  padding-top: 75.8204px;
  padding-bottom: 75.8204px;
  margin-right: auto;
  margin-left: auto;
}

.c-footer-landing__nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 31.4776px;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
  grid-template-rows: auto;
  box-sizing: border-box;
}

.c-footer-landing__group {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-sizing: border-box;
  width: 297.527px;
}

.c-footer-landing__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 45px;
  height: 32px;
  max-width: 100%;
  overflow-x: hidden;
  overflow-y: hidden;
  background-color: currentcolor;
}

.c-footer-landing__group-2 {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;
  gap: 12px;
  box-sizing: border-box;
  width: 100%;
}

.c-footer-landing__group-3 {
  display: block;
  box-sizing: border-box;
  color: #b0aea5;
}

.c-footer-landing__text-2 {
  display: inline;
  box-sizing: border-box;
}

.c-footer-landing__list {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: "";
}

.c-footer-landing__nav-item {
  display: flex;
  box-sizing: border-box;
}

.c-footer-landing__nav-link {
  display: block;
  box-sizing: border-box;
  max-width: 100%;
  color: #b0aea5;
  cursor: pointer;
  text-decoration-line: none;
  transition: color 0.2s ease;
}

.c-footer-landing__group-4 {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  width: 24px;
  height: 24px;
}

.c-footer-landing__columns {
  display: grid;
  justify-content: space-between;
  flex-grow: 1;
  flex-basis: 0%;
  gap: 31.4776px;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: auto;
  box-sizing: border-box;
}

.c-footer-landing__column {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  flex-basis: 0%;
  gap: 46.4327px;
  box-sizing: border-box;
  position: relative;
}

.c-footer-landing__group-5 {
  display: block;
  box-sizing: border-box;
}

.c-footer-landing__column-heading {
  display: flow-root;
  box-sizing: border-box;
  margin: 0px 0px 8px;
  font-size: 12px;
  font-weight: 500;
}

.c-footer-landing__column-heading::before {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -4.31844px;
}

.c-footer-landing__column-heading::after {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -3.59844px;
}

.c-footer-landing__list-2 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-footer-landing__nav-item-2 {
  display: flex;
  box-sizing: border-box;
  padding-top: 4px;
  padding-bottom: 8px;
}

.c-footer-landing__nav-link-2 {
  display: block;
  box-sizing: border-box;
  max-width: 100%;
  color: #b0aea5;
  cursor: pointer;
  letter-spacing: -0.24px;
  text-decoration-line: none;
  transition: color 0.2s ease;
}

.c-footer-landing__nav-link:hover {
  color: #faf9f5;
}

.c-footer-landing__nav-link:focus {
  outline: 2px solid #faf9f5;
  outline-offset: 4px;
}

.c-footer-landing__nav-link-2:hover {
  color: #faf9f5;
  text-decoration-line: underline;
  text-decoration-color: #faf9f5;
}

.c-footer-landing__nav-link-2:focus {
  outline: 2px solid #faf9f5;
  outline-offset: 4px;
}
```

**Mobile anatomy**

- `footer-landing-mobile`: the component root, a `<footer>` (`.c-footer-landing-mobile`)
- `footer-landing-mobile-heading`: heading, 6 characters (`.c-footer-landing-mobile__heading`)
- `footer-landing-mobile-inner`: inner block (`.c-footer-landing-mobile__inner`)
- `footer-landing-mobile-nav`: inner flex column (`.c-footer-landing-mobile__nav`), content not captured
- `footer-landing-mobile-group`: inner flex column (`.c-footer-landing-mobile__group`)
- `footer-landing-mobile-icon`: icon placeholder, 45x32px (`.c-footer-landing-mobile__icon`)
- `footer-landing-mobile-columns`: inner grid (`.c-footer-landing-mobile__columns`), content not captured
- `footer-landing-mobile-column`: inner flex column (`.c-footer-landing-mobile__column`, 3 instances), content not captured
- `footer-landing-mobile-group-2`: inner block (`.c-footer-landing-mobile__group-2`, 5 instances)
- `footer-landing-mobile-column-heading`: heading, 8 characters (`.c-footer-landing-mobile__column-heading`, 5 instances)
- `footer-landing-mobile-list`: inner flex column (`.c-footer-landing-mobile__list`, 5 instances), content not captured
- `footer-landing-mobile-nav-item`: inner flex row (`.c-footer-landing-mobile__nav-item`, 48 instances), content not captured
- `footer-landing-mobile-nav-link`: link (`.c-footer-landing-mobile__nav-link`, 47 instances), content not captured

**Mobile recipe**

```html
<div class="c-footer-landing-mobile-scope">
  <footer class="c-footer-landing-mobile">
    <h2 class="c-footer-landing-mobile__heading">lorem</h2>
    <div class="c-footer-landing-mobile__inner">
      <nav class="c-footer-landing-mobile__nav">
        <div class="c-footer-landing-mobile__group">
          <span class="c-footer-landing-mobile__icon" aria-hidden="true"></span>
        </div>
        <div class="c-footer-landing-mobile__columns">
          <section class="c-footer-landing-mobile__column">
            <div class="c-footer-landing-mobile__group-2">
              <h3 class="c-footer-landing-mobile__column-heading">lorem ip</h3>
              <ul class="c-footer-landing-mobile__list">
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
              </ul>
            </div>
            <div class="c-footer-landing-mobile__group-2">
              <h3 class="c-footer-landing-mobile__column-heading">lorem</h3>
              <ul class="c-footer-landing-mobile__list">
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
              </ul>
            </div>
          </section>
          <section class="c-footer-landing-mobile__column">
            <div class="c-footer-landing-mobile__group-2">
              <h3 class="c-footer-landing-mobile__column-heading">lorem ips</h3>
              <ul class="c-footer-landing-mobile__list">
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
              </ul>
            </div>
            <div class="c-footer-landing-mobile__group-2">
              <h3 class="c-footer-landing-mobile__column-heading">
                lorem ipsum dol
              </h3>
              <ul class="c-footer-landing-mobile__list">
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
              </ul>
            </div>
          </section>
          <section class="c-footer-landing-mobile__column">
            <div class="c-footer-landing-mobile__group-2">
              <h3 class="c-footer-landing-mobile__column-heading">lorem ips</h3>
              <ul class="c-footer-landing-mobile__list">
                <li class="c-footer-landing-mobile__nav-item">
                  <a class="c-footer-landing-mobile__nav-link" href="#"></a>
                </li>
                <li class="c-footer-landing-mobile__nav-item"></li>
              </ul>
            </div>
          </section>
        </div>
      </nav>
    </div>
  </footer>
</div>
```

```css
.c-footer-landing-mobile-scope {
  background-color: #f0eee6;
  color: #141413;
  font-family: "Anthropic Serif", Georgia, sans-serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
}

.c-footer-landing-mobile {
  display: inline-block;
  border-spacing: 0px;
  box-sizing: border-box;
  position: relative;
  background-color: #141413;
  color: #faf9f5;
  font-family: "Anthropic Sans", Arial, sans-serif;
  font-size: 12px;
  font-weight: 400;
  line-height: 16.8px;
}

.c-footer-landing-mobile__heading {
  display: flow-root;
  box-sizing: border-box;
  width: 1px;
  height: 1px;
  margin: 0px auto;
  position: absolute;
  top: 0%;
  right: 0%;
  left: 0%;
  overflow-x: hidden;
  overflow-y: hidden;
  font-size: 12px;
  font-weight: 400;
  white-space: nowrap;
}

.c-footer-landing-mobile__heading::before {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -4.31844px;
}

.c-footer-landing-mobile__heading::after {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -3.59844px;
}

.c-footer-landing-mobile__inner {
  display: block;
  box-sizing: border-box;
  width: 100%;
  max-width: 324.824px;
  position: relative;
  padding-top: 48.3918px;
  padding-bottom: 48.3918px;
  margin-right: auto;
  margin-left: auto;
}

.c-footer-landing-mobile__nav {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 48.3918px;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
  grid-template-rows: auto;
  box-sizing: border-box;
}

.c-footer-landing-mobile__group {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-sizing: border-box;
  width: 89.5755px;
}

.c-footer-landing-mobile__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 45px;
  height: 32px;
  max-width: 100%;
  overflow-x: hidden;
  overflow-y: hidden;
  background-color: currentcolor;
}

.c-footer-landing-mobile__columns {
  display: grid;
  flex-direction: column;
  justify-content: space-between;
  flex-grow: 1;
  flex-basis: 0%;
  gap: 28.049px;
  grid-template-columns: 1fr;
  grid-template-rows: auto;
  box-sizing: border-box;
}

.c-footer-landing-mobile__column {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  flex-basis: 0%;
  gap: 28.049px;
  box-sizing: border-box;
  position: relative;
}

.c-footer-landing-mobile__group-2 {
  display: block;
  flex-grow: 1;
  flex-basis: 0%;
  box-sizing: border-box;
}

.c-footer-landing-mobile__column-heading {
  display: flow-root;
  box-sizing: border-box;
  margin: 0px 0px 8px;
  font-size: 12px;
  font-weight: 500;
}

.c-footer-landing-mobile__column-heading::before {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -4.31844px;
}

.c-footer-landing-mobile__column-heading::after {
  content: "";
  display: table;
  box-sizing: border-box;
  margin-bottom: -3.59844px;
}

.c-footer-landing-mobile__list {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-footer-landing-mobile__nav-item {
  display: flex;
  box-sizing: border-box;
  padding-top: 4px;
  padding-bottom: 8px;
}

.c-footer-landing-mobile__nav-link {
  display: block;
  box-sizing: border-box;
  max-width: 100%;
  color: #b0aea5;
  cursor: pointer;
  letter-spacing: -0.24px;
  text-decoration-line: none;
  transition: color 0.2s ease;
}

.c-footer-landing-mobile__nav-link:hover {
  color: #faf9f5;
  text-decoration-line: underline;
  text-decoration-color: #faf9f5;
  text-decoration-thickness: auto;
  text-underline-offset: 3px;
}

.c-footer-landing-mobile__nav-link:focus {
  outline: 2px solid #faf9f5;
  outline-offset: 4px;
}
```

**States**

- `footer-landing-nav-link` hover (`footer-landing-nav-link-hover`): color #FAF9F5
- `footer-landing-nav-link` focus: outline 2px solid #FAF9F5, outline-offset 4px
- `footer-landing-nav-link-2` hover (`footer-landing-nav-link-2-hover`): color #FAF9F5, text-decoration-line underline, text-decoration-color #FAF9F5
- `footer-landing-nav-link-2` focus: outline 2px solid #FAF9F5, outline-offset 4px
- mobile, `footer-landing-mobile-nav-link` hover (`footer-landing-mobile-nav-link-hover`): color #FAF9F5, text-decoration-line underline, text-decoration-color #FAF9F5, text-decoration-thickness auto, text-underline-offset 3px
- mobile, `footer-landing-mobile-nav-link` focus: outline 2px solid #FAF9F5, outline-offset 4px

### Button, primary (2)

**Verification**: flagged, the render matched 96% of the original pixels, below the 97% required after 2 correction attempts.

**Anatomy**

- `button-primary-2`: the component root, a `<a>` (`.c-button-primary-2`), 10-character label

**Recipe**

```html
<div class="c-button-primary-2-scope">
  <a class="c-button-primary-2" href="#">lorem ipsu</a>
</div>
```

```css
.c-button-primary-2-scope {
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-button-primary-2 {
  display: inline-block;
  border-spacing: 0px;
  box-sizing: border-box;
  height: 36px;
  padding: 8px 16px;
  background-color: #0f0f0e;
  color: #faf9f5;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  text-decoration-line: none;
  transition: background-color 0.2s ease;
  border-top-left-radius: 8px;
  border-bottom-left-radius: 8px;
}

.c-button-primary-2:hover {
  background-color: #000000cc;
}
```

**States**

- hover (`button-primary-2-hover`): background-color #000000CC

### Button, primary (3)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `button-primary-3`: the component root, a `<a>` (`.c-button-primary-3`)
- `button-primary-3-label`: label text, 14 characters (`.c-button-primary-3__label`)

**Recipe**

```html
<div class="c-button-primary-3-scope">
  <a class="c-button-primary-3" href="#">
    <span class="c-button-primary-3__label">lorem ipsum do</span>
  </a>
</div>
```

```css
.c-button-primary-3-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-button-primary-3 {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  height: 40px;
  min-width: 44px;
  padding: 8px 16px;
  background-color: #141413;
  color: #faf9f5;
  border: 1px solid #141413;
  border-radius: 8px;
  cursor: pointer;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
  text-decoration-line: none;
  transition-duration: 0.2s, 0.2s;
  transition-timing-function:
    cubic-bezier(0.77, 0, 0.175, 1), cubic-bezier(0.77, 0, 0.175, 1);
  transition-property: background-color, color;
}

.c-button-primary-3__label {
  display: block;
  box-sizing: border-box;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  line-height: 21px;
}

.c-button-primary-3:hover {
  background-color: #3d3d3a;
}
```

**States**

- hover (`button-primary-3-hover`): background-color #3D3D3A

### Button, secondary

**Verification**: verified against the live page at desktop.

**Anatomy**

- `button-secondary`: the component root, a `<a>` (`.c-button-secondary`)
- `button-secondary-label`: label text, 14 characters (`.c-button-secondary__label`)

**Recipe**

```html
<div class="c-button-secondary-scope">
  <a class="c-button-secondary" href="#">
    <span class="c-button-secondary__label">lorem ipsum do</span>
  </a>
</div>
```

```css
.c-button-secondary-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-button-secondary {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  height: 40px;
  min-width: 44px;
  padding: 8px 16px;
  color: #141413;
  border: 1px solid #141413;
  border-radius: 8px;
  cursor: pointer;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
  text-decoration-line: none;
  transition-duration: 0.2s, 0.2s;
  transition-timing-function:
    cubic-bezier(0.77, 0, 0.175, 1), cubic-bezier(0.77, 0, 0.175, 1);
  transition-property: background-color, color;
}

.c-button-secondary__label {
  display: block;
  box-sizing: border-box;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  line-height: 21px;
}

.c-button-secondary:hover {
  background-color: #141413;
  color: #faf9f5;
}
```

**States**

- hover (`button-secondary-hover`): background-color #141413, color #FAF9F5

### Button, secondary (2)

**Verification**: flagged, the `button-secondary-2-icon` x did not reproduce the measured 128px after 2 correction attempts.

**Anatomy**

- `button-secondary-2`: the component root, a `<a>` (`.c-button-secondary-2`)
- `button-secondary-2-label`: label text, 14 characters (`.c-button-secondary-2__label`)
- `button-secondary-2-group`: inner flex row (`.c-button-secondary-2__group`)
- `button-secondary-2-icon`: icon placeholder, 20px (`.c-button-secondary-2__icon`)

**Recipe**

```html
<div class="c-button-secondary-2-scope">
  <a class="c-button-secondary-2" href="#">
    <span class="c-button-secondary-2__label">lorem ipsum do</span>
    <span class="c-button-secondary-2__group">
      <span class="c-button-secondary-2__icon" aria-hidden="true"></span>
    </span>
  </a>
</div>
```

```css
.c-button-secondary-2-scope {
  background-color: #141413;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-button-secondary-2 {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  width: fit-content;
  height: 36px;
  min-width: 44px;
  padding: 8px 12px 8px 16px;
  background-color: #faf9f5;
  color: #141413;
  border: 1px solid #faf9f5;
  border-radius: 8px;
  cursor: pointer;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
  text-decoration-line: none;
  transition-duration: 0.2s, 0.2s;
  transition-timing-function:
    cubic-bezier(0.77, 0, 0.175, 1), cubic-bezier(0.77, 0, 0.175, 1);
  transition-property: background-color, color;
}

.c-button-secondary-2__label {
  display: block;
  box-sizing: border-box;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  line-height: 21px;
}

.c-button-secondary-2__group {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
}

.c-button-secondary-2__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 20px;
  height: 20px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
}

.c-button-secondary-2:hover {
  background-color: #f0eee6;
}
```

**States**

- hover (`button-secondary-2-hover`): background-color #F0EEE6

### Card (2)

**Verification**: verified against the live page at desktop.

**Anatomy**

- Group: 6 instances in a 1-column grid; the recipe carries the values they all share
- `card-2`: the component root, a `<article>` (`.c-card-2`)
- `card-2-link`: link (`.c-card-2__link`)
- `card-2-group`: inner flex row (`.c-card-2__group`)
- `card-2-title`: heading, 47 characters (`.c-card-2__title`)
- `card-2-text`: label text, 12 characters (`.c-card-2__text`)

**Recipe**

```html
<div class="c-card-2-scope">
  <article class="c-card-2">
    <a class="c-card-2__link" href="#">
      <div class="c-card-2__group">
        <h3 class="c-card-2__title">
          lorem ipsum dolor sit amet consectetur adipisci
        </h3>
        <div class="c-card-2__text">lorem ipsum</div>
      </div>
    </a>
  </article>
</div>
```

```css
.c-card-2-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-card-2 {
  display: block;
  border-spacing: 0px;
  box-sizing: border-box;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
  padding-top: 24px;
  padding-bottom: 24px;
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: #87867f;
}

.c-card-2__link {
  display: flex;
  align-items: center;
  gap: 16px;
  box-sizing: border-box;
  color: #0f0f0e;
  cursor: pointer;
  text-decoration-line: none;
}

.c-card-2__group {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-grow: 1;
  flex-basis: 0%;
  gap: 12px;
  box-sizing: border-box;
}

.c-card-2__title {
  display: block;
  box-sizing: border-box;
  margin: 0px;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 32px;
  font-weight: 600;
  line-height: 38.4px;
}

.c-card-2__text {
  display: block;
  box-sizing: border-box;
  color: #141413;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 17px;
  line-height: 26.35px;
  white-space: nowrap;
}
```

**States**

- No hover or focus change was observed.

### Footer nav

**Verification**: flagged, the `footer-nav` height did not reproduce the measured 975px after 2 correction attempts.

**Anatomy**

- `footer-nav`: the component root, a `<nav>` (`.c-footer-nav`), content not captured
- `footer-nav-group`: inner flex column (`.c-footer-nav__group`, 2 instances), content not captured
- `footer-nav-group-2`: inner flex column (`.c-footer-nav__group-2`, 3 instances)
- `footer-nav-title`: heading, 8 characters (`.c-footer-nav__title`, 3 instances)
- `footer-nav-list`: inner flex column (`.c-footer-nav__list`, 3 instances), content not captured
- `footer-nav-item`: inner group (`.c-footer-nav__item`, 28 instances), content not captured

**Recipe**

```html
<div class="c-footer-nav-scope">
  <nav class="c-footer-nav">
    <div class="c-footer-nav__group">
      <div class="c-footer-nav__group-2">
        <h3 class="c-footer-nav__title">lorem ip</h3>
        <ul class="c-footer-nav__list">
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
        </ul>
      </div>
      <div class="c-footer-nav__group-2">
        <h3 class="c-footer-nav__title">lorem</h3>
        <ul class="c-footer-nav__list">
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
        </ul>
      </div>
    </div>
    <div class="c-footer-nav__group">
      <div class="c-footer-nav__group-2">
        <h3 class="c-footer-nav__title">lorem ips</h3>
        <ul class="c-footer-nav__list">
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
          <li class="c-footer-nav__item"></li>
        </ul>
      </div>
    </div>
  </nav>
</div>
```

```css
.c-footer-nav-scope {
  background-color: #141413;
  color: #faf9f5;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-footer-nav {
  display: inline-grid;
  gap: 32px;
  grid-template-columns: repeat(4, 1fr);
  border-spacing: 0px;
  box-sizing: border-box;
  color: #faf9f5;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
}

.c-footer-nav__group {
  display: flex;
  flex-direction: column;
  gap: 48px;
  box-sizing: border-box;
}

.c-footer-nav__group-2 {
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-sizing: border-box;
  width: 100%;
}

.c-footer-nav__title {
  display: block;
  box-sizing: border-box;
  margin: 0px;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 12px;
  font-weight: 700;
  line-height: 16.8px;
}

.c-footer-nav__list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-footer-nav__item {
  display: list-item;
  box-sizing: border-box;
}
```

**States**

- No hover or focus change was observed.

### Nav dropdown (4)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `nav-dropdown-4`: the component root, a `<button>` (`.c-nav-dropdown-4`)
- `nav-dropdown-4-text`: label text, 8 characters (`.c-nav-dropdown-4__text`)
- `nav-dropdown-4-icon`: icon placeholder, 12x6px (`.c-nav-dropdown-4__icon`)

**Recipe**

```html
<div class="c-nav-dropdown-4-scope">
  <button class="c-nav-dropdown-4" type="button">
    <span class="c-nav-dropdown-4__text">lorem ip</span>
    <span class="c-nav-dropdown-4__icon" aria-hidden="true"></span>
  </button>
</div>
```

```css
.c-nav-dropdown-4-scope {
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
}

.c-nav-dropdown-4 {
  display: flex;
  align-items: center;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
  list-style-type: none;
}

.c-nav-dropdown-4__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-nav-dropdown-4:hover {
  text-decoration-line: underline;
}
```

**States**

- hover: text-decoration-line underline

### Nav dropdown (5)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `nav-dropdown-5`: the component root, a `<button>` (`.c-nav-dropdown-5`)
- `nav-dropdown-5-text`: label text, 11 characters (`.c-nav-dropdown-5__text`)
- `nav-dropdown-5-icon`: icon placeholder, 12x6px (`.c-nav-dropdown-5__icon`)

**Recipe**

```html
<div class="c-nav-dropdown-5-scope">
  <button class="c-nav-dropdown-5" type="button">
    <span class="c-nav-dropdown-5__text">lorem ipsum</span>
    <span class="c-nav-dropdown-5__icon" aria-hidden="true"></span>
  </button>
</div>
```

```css
.c-nav-dropdown-5-scope {
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
}

.c-nav-dropdown-5 {
  display: flex;
  align-items: center;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
  list-style-type: none;
}

.c-nav-dropdown-5__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-nav-dropdown-5:hover {
  text-decoration-line: underline;
}
```

**States**

- hover: text-decoration-line underline

### Nav dropdown (6)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `nav-dropdown-6`: the component root, a `<button>` (`.c-nav-dropdown-6`)
- `nav-dropdown-6-text`: label text, 5 characters (`.c-nav-dropdown-6__text`)
- `nav-dropdown-6-icon`: icon placeholder, 12x6px (`.c-nav-dropdown-6__icon`)

**Recipe**

```html
<div class="c-nav-dropdown-6-scope">
  <button class="c-nav-dropdown-6" type="button">
    <span class="c-nav-dropdown-6__text">lorem</span>
    <span class="c-nav-dropdown-6__icon" aria-hidden="true"></span>
  </button>
</div>
```

```css
.c-nav-dropdown-6-scope {
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
}

.c-nav-dropdown-6 {
  display: flex;
  align-items: center;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
  list-style-type: none;
}

.c-nav-dropdown-6__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-nav-dropdown-6:hover {
  text-decoration-line: underline;
}
```

**States**

- hover: text-decoration-line underline

### Social links

**Verification**: verified against the live page at desktop.

**Anatomy**

- `social-link`: the component root, a `<ul>` (`.c-social-link`)
- `social-link-item`: inner group (`.c-social-link__item`, 3 instances)
- `social-link-link`: link (`.c-social-link__link`, 3 instances)
- `social-link-icon`: icon placeholder, 24px (`.c-social-link__icon`, 3 instances)

**Recipe**

```html
<div class="c-social-link-scope">
  <ul class="c-social-link">
    <li class="c-social-link__item">
      <a class="c-social-link__link" href="#">
        <span class="c-social-link__icon" aria-hidden="true"></span>
      </a>
    </li>
    <li class="c-social-link__item">
      <a class="c-social-link__link" href="#">
        <span class="c-social-link__icon" aria-hidden="true"></span>
      </a>
    </li>
    <li class="c-social-link__item">
      <a class="c-social-link__link" href="#">
        <span class="c-social-link__icon" aria-hidden="true"></span>
      </a>
    </li>
  </ul>
</div>
```

```css
.c-social-link-scope {
  background-color: #141413;
  color: #faf9f5;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-social-link {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 0px;
  color: #faf9f5;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
  list-style-type: none;
}

.c-social-link__item {
  display: list-item;
  box-sizing: border-box;
}

.c-social-link__link {
  display: inline;
  box-sizing: border-box;
  color: #141413;
  cursor: pointer;
  text-decoration-line: underline;
  text-decoration-color: #141413;
  transition: color 0.1s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.c-social-link__icon {
  display: inline-block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 24px;
  height: 24px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
}
```

**States**

- No hover or focus change was observed.

### Header (inner)

**Verification**: desktop verified against the live page at desktop; mobile verified against the live page at mobile.

Variant observed on https://www.anthropic.com/engineering.

**Anatomy**

- `header-inner`: the component root, a `<header>` (`.c-header-inner`)
- `header-inner-inner`: inner flex row (`.c-header-inner__inner`)
- `header-inner-logo`: link (`.c-header-inner__logo`)
- `header-inner-group`: inner flex row (`.c-header-inner__group`)
- `header-inner-group-2`: inner block (`.c-header-inner__group-2`)
- `header-inner-logo-icon`: icon placeholder, 143x16px (`.c-header-inner__logo-icon`)
- `header-inner-group-3`: inner flex row (`.c-header-inner__group-3`)
- `header-inner-nav`: inner flex row (`.c-header-inner__nav`)
- `header-inner-nav-list`: inner flex row (`.c-header-inner__nav-list`)
- `header-inner-nav-item`: inner group (`.c-header-inner__nav-item`, 5 instances)
- `header-inner-button`: button (`.c-header-inner__button`, 3 instances)
- `header-inner-text`: label text, 8 characters (`.c-header-inner__text`, 3 instances)
- `header-inner-button-icon`: icon placeholder, 12x6px (`.c-header-inner__button-icon`, 3 instances)
- `header-inner-nav-link`: link, 6-character label (`.c-header-inner__nav-link`, 2 instances)
- `header-inner-group-4`: inner flex row (`.c-header-inner__group-4`)
- `header-inner-cta`: the `button-primary-2` button, 10-character label (`.c-header-inner__cta`)
- `header-inner-group-5`: inner flex row (`.c-header-inner__group-5`)
- `header-inner-icon`: icon placeholder, 12x6px (`.c-header-inner__icon`)

**Desktop recipe**

```html
<div class="c-header-inner-scope">
  <header class="c-header-inner">
    <div class="c-header-inner__inner">
      <a class="c-header-inner__logo" href="#">
        <div class="c-header-inner__group">
          <div class="c-header-inner__group-2">
            <span class="c-header-inner__logo-icon" aria-hidden="true"></span>
          </div>
        </div>
      </a>
      <div class="c-header-inner__group-3">
        <nav class="c-header-inner__nav">
          <ul class="c-header-inner__nav-list">
            <li class="c-header-inner__nav-item">
              <button class="c-header-inner__button" type="button">
                <span class="c-header-inner__text">lorem ip</span>
                <span
                  class="c-header-inner__button-icon"
                  aria-hidden="true"
                ></span>
              </button>
            </li>
            <li class="c-header-inner__nav-item">
              <a class="c-header-inner__nav-link" href="#">lorem</a>
            </li>
            <li class="c-header-inner__nav-item">
              <button class="c-header-inner__button" type="button">
                <span class="c-header-inner__text">lorem ipsum</span>
                <span
                  class="c-header-inner__button-icon"
                  aria-hidden="true"
                ></span>
              </button>
            </li>
            <li class="c-header-inner__nav-item">
              <button class="c-header-inner__button" type="button">
                <span class="c-header-inner__text">lorem</span>
                <span
                  class="c-header-inner__button-icon"
                  aria-hidden="true"
                ></span>
              </button>
            </li>
            <li class="c-header-inner__nav-item">
              <a class="c-header-inner__nav-link" href="#">lore</a>
            </li>
          </ul>
        </nav>
        <div class="c-header-inner__group-4">
          <a class="c-header-inner__cta" href="#">lorem ipsu</a>
          <div class="c-header-inner__group-5">
            <span class="c-header-inner__icon" aria-hidden="true"></span>
          </div>
        </div>
      </div>
    </div>
  </header>
</div>
```

```css
.c-header-inner-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-header-inner {
  display: block;
  border-spacing: 0px;
  box-sizing: border-box;
  position: sticky;
  top: 0px;
  z-index: 9999;
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
  padding-top: 16px;
  padding-bottom: 16px;
}

.c-header-inner__inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-sizing: border-box;
  width: 100%;
  max-width: 1400px;
  padding-right: 64px;
  padding-left: 64px;
  margin-right: auto;
  margin-left: auto;
}

.c-header-inner__logo {
  display: block;
  box-sizing: border-box;
  color: #141413;
  cursor: pointer;
  text-decoration-line: underline;
  text-decoration-color: #141413;
  transition: color 0.1s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.c-header-inner__group {
  display: flex;
  align-items: center;
  box-sizing: border-box;
  width: 143px;
  height: 16px;
  position: relative;
}

.c-header-inner__group-2 {
  display: block;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  position: relative;
}

.c-header-inner__logo-icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 143px;
  height: 16px;
  position: absolute;
  top: 0px;
  right: 0px;
  bottom: 0px;
  left: 0px;
  overflow-x: hidden;
  overflow-y: hidden;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 0);
}

.c-header-inner__group-3 {
  display: flex;
  align-items: center;
  gap: 24px;
  box-sizing: border-box;
  margin-left: auto;
}

.c-header-inner__nav {
  display: flex;
  align-items: center;
  box-sizing: border-box;
}

.c-header-inner__nav-list {
  display: flex;
  gap: 24px;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-header-inner__nav-item {
  display: list-item;
  box-sizing: border-box;
  position: relative;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  line-height: 21px;
}

.c-header-inner__button {
  display: flex;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
}

.c-header-inner__button-icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-header-inner__nav-link {
  display: flex;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  color: #0f0f0e;
  cursor: pointer;
  letter-spacing: -0.0375px;
  text-decoration-line: none;
  white-space: nowrap;
}

.c-header-inner__group-4 {
  display: flex;
  box-sizing: border-box;
  position: relative;
}

.c-header-inner__cta {
  display: block;
  box-sizing: border-box;
  height: 36px;
  padding: 8px 16px;
  background-color: #0f0f0e;
  color: #faf9f5;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  line-height: 21px;
  text-decoration-line: none;
  transition: background-color 0.2s ease;
  border-top-left-radius: 8px;
  border-bottom-left-radius: 8px;
}

.c-header-inner__group-5 {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  padding: 12px 16px;
  position: relative;
  background-color: #0f0f0e;
  color: #faf9f5;
  cursor: pointer;
  transition: background-color 0.2s ease;
  border-left-width: 1px;
  border-left-style: solid;
  border-left-color: #ffffff33;
  border-top-right-radius: 8px;
  border-bottom-right-radius: 8px;
}

.c-header-inner__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transition: transform 0.2s ease-in-out;
}

.c-header-inner__logo:hover {
  color: #87867f;
  text-decoration-color: #87867f;
}

.c-header-inner__logo:focus {
  color: #87867f;
  outline: none;
  text-decoration-color: #87867f;
}

.c-header-inner__button:hover {
  text-decoration-line: underline;
}

.c-header-inner__nav-link:hover {
  text-decoration-line: underline;
}

.c-header-inner__cta:hover {
  background-color: #000000cc;
}
```

**Mobile anatomy**

- `header-inner-mobile`: the component root, a `<header>` (`.c-header-inner-mobile`)
- `header-inner-mobile-inner`: inner flex row (`.c-header-inner-mobile__inner`)
- `header-inner-mobile-logo`: link (`.c-header-inner-mobile__logo`)
- `header-inner-mobile-logo-icon`: icon placeholder, 32px (`.c-header-inner-mobile__logo-icon`)
- `header-inner-mobile-group`: inner flex row (`.c-header-inner-mobile__group`)
- `header-inner-mobile-menu-toggle`: button (`.c-header-inner-mobile__menu-toggle`)
- `header-inner-mobile-menu-toggle-icon`: icon placeholder, 24px (`.c-header-inner-mobile__menu-toggle-icon`)

**Mobile recipe**

```html
<div class="c-header-inner-mobile-scope">
  <header class="c-header-inner-mobile">
    <div class="c-header-inner-mobile__inner">
      <a class="c-header-inner-mobile__logo" href="#">
        <span
          class="c-header-inner-mobile__logo-icon"
          aria-hidden="true"
        ></span>
      </a>
      <div class="c-header-inner-mobile__group">
        <button class="c-header-inner-mobile__menu-toggle" type="button">
          <span
            class="c-header-inner-mobile__menu-toggle-icon"
            aria-hidden="true"
          ></span>
        </button>
      </div>
    </div>
  </header>
</div>
```

```css
.c-header-inner-mobile-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-header-inner-mobile {
  display: block;
  border-spacing: 0px;
  box-sizing: border-box;
  position: sticky;
  top: 0px;
  z-index: 9999;
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
  padding-top: 16px;
  padding-bottom: 16px;
}

.c-header-inner-mobile__inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-sizing: border-box;
  width: 100%;
  max-width: 1400px;
  padding-right: 32px;
  padding-left: 32px;
  margin-right: auto;
  margin-left: auto;
}

.c-header-inner-mobile__logo {
  display: block;
  box-sizing: border-box;
  color: #141413;
  cursor: pointer;
  text-decoration-line: underline;
  text-decoration-color: #141413;
  transition: color 0.1s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.c-header-inner-mobile__logo-icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 32px;
  height: 32px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
}

.c-header-inner-mobile__group {
  display: flex;
  align-items: center;
  gap: 24px;
  box-sizing: border-box;
  margin-left: auto;
}

.c-header-inner-mobile__menu-toggle {
  display: flex;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #141413;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: normal;
  text-transform: none;
  text-align: center;
}

.c-header-inner-mobile__menu-toggle-icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 24px;
  height: 24px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
}

.c-header-inner-mobile__logo:hover {
  color: #87867f;
  text-decoration-color: #87867f;
}

.c-header-inner-mobile__logo:focus {
  color: #87867f;
  outline: none;
  text-decoration-color: #87867f;
}
```

**States**

- `header-inner-logo` hover (`header-inner-logo-hover`): color #87867F, text-decoration-color #87867F
- `header-inner-logo` focus (`header-inner-logo-focus`): color #87867F, outline none, text-decoration-color #87867F
- `header-inner-button` hover: text-decoration-line underline
- `header-inner-nav-link` hover: text-decoration-line underline
- `header-inner-cta` hover (`header-inner-cta-hover`): background-color #000000CC
- mobile, `header-inner-mobile-logo` hover (`header-inner-mobile-logo-hover`): color #87867F, text-decoration-color #87867F
- mobile, `header-inner-mobile-logo` focus (`header-inner-mobile-logo-focus`): color #87867F, outline none, text-decoration-color #87867F

### Footer (inner)

**Verification**: desktop flagged, the `footer-inner` height did not reproduce the measured 1103px after 2 correction attempts; mobile flagged, the `footer-inner-mobile-inner` height did not reproduce the measured 3651px after 2 correction attempts.

Variant observed on https://www.anthropic.com/engineering.

**Anatomy**

- `footer-inner`: the component root, a `<footer>` (`.c-footer-inner`)
- `footer-inner-columns`: inner grid (`.c-footer-inner__columns`), content not captured
- `footer-inner-column`: inner block (`.c-footer-inner__column`)
- `footer-inner-link`: link (`.c-footer-inner__link`)
- `footer-inner-link-icon`: icon placeholder, 46x32px (`.c-footer-inner__link-icon`)
- `footer-inner-nav`: inner grid (`.c-footer-inner__nav`), content not captured
- `footer-inner-group`: inner flex column (`.c-footer-inner__group`, 3 instances), content not captured
- `footer-inner-group-2`: inner flex column (`.c-footer-inner__group-2`, 5 instances)
- `footer-inner-heading`: heading, 8 characters (`.c-footer-inner__heading`, 5 instances)
- `footer-inner-list`: inner flex column (`.c-footer-inner__list`, 5 instances), content not captured
- `footer-inner-nav-item`: inner group (`.c-footer-inner__nav-item`, 48 instances)
- `footer-inner-nav-link`: link, 6-character label (`.c-footer-inner__nav-link`, 48 instances)

**Desktop recipe**

```html
<div class="c-footer-inner-scope">
  <footer class="c-footer-inner">
    <div class="c-footer-inner__columns">
      <div class="c-footer-inner__column">
        <a class="c-footer-inner__link" href="#">
          <span class="c-footer-inner__link-icon" aria-hidden="true"></span>
        </a>
      </div>
      <nav class="c-footer-inner__nav">
        <div class="c-footer-inner__group">
          <div class="c-footer-inner__group-2">
            <h3 class="c-footer-inner__heading">lorem ip</h3>
            <ul class="c-footer-inner__list">
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsum</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#"
                  >lorem ipsum dolor sit</a
                >
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsum d</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem i</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsum d</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsum do</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsum dol</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#"
                  >lorem ipsum dolo</a
                >
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#"
                  >lorem ipsum dolor sit am</a
                >
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsum</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem i</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#"
                  >lorem ipsum dolo</a
                >
              </li>
            </ul>
          </div>
          <div class="c-footer-inner__group-2">
            <h3 class="c-footer-inner__heading">lorem</h3>
            <ul class="c-footer-inner__list">
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lore</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem</a>
              </li>
            </ul>
          </div>
        </div>
        <div class="c-footer-inner__group">
          <div class="c-footer-inner__group-2">
            <h3 class="c-footer-inner__heading">lorem ips</h3>
            <ul class="c-footer-inner__list">
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ips</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#"
                  >lorem ipsum dolor</a
                >
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ip</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#"
                  >lorem ipsum dolo</a
                >
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsum d</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsu</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#"
                  >lorem ipsum dolor</a
                >
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsu</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsu</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#"
                  >lorem ipsum dolo</a
                >
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsum d</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsum d</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsu</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsum do</a>
              </li>
            </ul>
          </div>
          <div class="c-footer-inner__group-2">
            <h3 class="c-footer-inner__heading">lorem ipsum dol</h3>
            <ul class="c-footer-inner__list">
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ip</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsum do</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem i</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ips</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsum</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#"
                  >lorem ipsum dolor s</a
                >
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsum d</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsum</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#"
                  >lorem ipsum dolor</a
                >
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lorem ipsum d</a>
              </li>
            </ul>
          </div>
        </div>
        <div class="c-footer-inner__group">
          <div class="c-footer-inner__group-2">
            <h3 class="c-footer-inner__heading">lorem ips</h3>
            <ul class="c-footer-inner__list">
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#">lore</a>
              </li>
              <li class="c-footer-inner__nav-item">
                <a class="c-footer-inner__nav-link" href="#"
                  >lorem ipsum dolor sit</a
                >
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </footer>
</div>
```

```css
.c-footer-inner-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-footer-inner {
  display: block;
  border-spacing: 0px;
  box-sizing: border-box;
  background-color: #141413;
  color: #faf9f5;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
}

.c-footer-inner__columns {
  display: grid;
  flex-direction: column;
  gap: 64px;
  grid-template-columns: repeat(11, 1fr);
  box-sizing: border-box;
  width: 100%;
  max-width: 1400px;
  padding: 64px;
  margin-right: auto;
  margin-left: auto;
}

.c-footer-inner__column {
  display: block;
  box-sizing: border-box;
}

.c-footer-inner__link {
  display: inline;
  box-sizing: border-box;
  color: #141413;
  cursor: pointer;
  text-decoration-line: underline;
  text-decoration-color: #141413;
  transition: color 0.1s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.c-footer-inner__link-icon {
  display: inline-block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 46px;
  height: 32px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
}

.c-footer-inner__nav {
  display: grid;
  gap: 32px;
  grid-template-columns: repeat(4, 1fr);
  box-sizing: border-box;
}

.c-footer-inner__group {
  display: flex;
  flex-direction: column;
  gap: 48px;
  box-sizing: border-box;
}

.c-footer-inner__group-2 {
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-sizing: border-box;
  width: 100%;
}

.c-footer-inner__heading {
  display: block;
  box-sizing: border-box;
  margin: 0px;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 12px;
  font-weight: 700;
  line-height: 16.8px;
}

.c-footer-inner__list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-footer-inner__nav-item {
  display: list-item;
  box-sizing: border-box;
}

.c-footer-inner__nav-link {
  display: inline;
  box-sizing: border-box;
  color: #b0aea5;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 12px;
  line-height: 16.8px;
  text-decoration-line: none;
}

.c-footer-inner__link:focus {
  color: #87867f;
  outline: none;
  text-decoration-color: #87867f;
}

.c-footer-inner__nav-link:hover {
  color: #ffffff;
  text-decoration-line: underline;
  text-decoration-color: #ffffff;
}
```

**Mobile anatomy**

- `footer-inner-mobile`: the component root, a `<footer>` (`.c-footer-inner-mobile`)
- `footer-inner-mobile-inner`: inner flex column (`.c-footer-inner-mobile__inner`), content not captured
- `footer-inner-mobile-group`: inner block (`.c-footer-inner-mobile__group`)
- `footer-inner-mobile-link`: link (`.c-footer-inner-mobile__link`)
- `footer-inner-mobile-link-icon`: icon placeholder, 46x32px (`.c-footer-inner-mobile__link-icon`)
- `footer-inner-mobile-nav`: inner group (`.c-footer-inner-mobile__nav`), content not captured
- `footer-inner-mobile-group-2`: inner flex column (`.c-footer-inner-mobile__group-2`, 3 instances), content not captured
- `footer-inner-mobile-group-3`: inner flex column (`.c-footer-inner-mobile__group-3`, 5 instances)
- `footer-inner-mobile-heading`: heading, 8 characters (`.c-footer-inner-mobile__heading`, 5 instances)
- `footer-inner-mobile-list`: inner flex column (`.c-footer-inner-mobile__list`, 5 instances), content not captured
- `footer-inner-mobile-nav-item`: inner group (`.c-footer-inner-mobile__nav-item`, 48 instances)
- `footer-inner-mobile-nav-link`: link, 6-character label (`.c-footer-inner-mobile__nav-link`, 48 instances)

**Mobile recipe**

```html
<div class="c-footer-inner-mobile-scope">
  <footer class="c-footer-inner-mobile">
    <div class="c-footer-inner-mobile__inner">
      <div class="c-footer-inner-mobile__group">
        <a class="c-footer-inner-mobile__link" href="#">
          <span
            class="c-footer-inner-mobile__link-icon"
            aria-hidden="true"
          ></span>
        </a>
      </div>
      <nav class="c-footer-inner-mobile__nav">
        <div class="c-footer-inner-mobile__group-2">
          <div class="c-footer-inner-mobile__group-3">
            <h3 class="c-footer-inner-mobile__heading">lorem ip</h3>
            <ul class="c-footer-inner-mobile__list">
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum dolor sit</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum d</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lorem i</a>
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum d</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum do</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum dol</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum dolo</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum dolor sit am</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lorem i</a>
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum dolo</a
                >
              </li>
            </ul>
          </div>
          <div class="c-footer-inner-mobile__group-3">
            <h3 class="c-footer-inner-mobile__heading">lorem</h3>
            <ul class="c-footer-inner-mobile__list">
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lore</a>
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lorem</a>
              </li>
            </ul>
          </div>
        </div>
        <div class="c-footer-inner-mobile__group-2">
          <div class="c-footer-inner-mobile__group-3">
            <h3 class="c-footer-inner-mobile__heading">lorem ips</h3>
            <ul class="c-footer-inner-mobile__list">
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ips</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum dolor</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lorem ip</a>
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum dolo</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum d</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsu</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum dolor</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsu</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsu</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum dolo</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum d</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum d</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsu</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lorem</a>
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum do</a
                >
              </li>
            </ul>
          </div>
          <div class="c-footer-inner-mobile__group-3">
            <h3 class="c-footer-inner-mobile__heading">lorem ipsum dol</h3>
            <ul class="c-footer-inner-mobile__list">
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lorem ip</a>
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum do</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lorem i</a>
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ips</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum dolor s</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum d</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum dolor</a
                >
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum d</a
                >
              </li>
            </ul>
          </div>
        </div>
        <div class="c-footer-inner-mobile__group-2">
          <div class="c-footer-inner-mobile__group-3">
            <h3 class="c-footer-inner-mobile__heading">lorem ips</h3>
            <ul class="c-footer-inner-mobile__list">
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#">lore</a>
              </li>
              <li class="c-footer-inner-mobile__nav-item">
                <a class="c-footer-inner-mobile__nav-link" href="#"
                  >lorem ipsum dolor sit</a
                >
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </footer>
</div>
```

```css
.c-footer-inner-mobile-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-footer-inner-mobile {
  display: block;
  border-spacing: 0px;
  box-sizing: border-box;
  background-color: #141413;
  color: #faf9f5;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
}

.c-footer-inner-mobile__inner {
  display: flex;
  flex-direction: column;
  gap: 64px;
  box-sizing: border-box;
  width: 100%;
  max-width: 1400px;
  padding: 32px;
  margin-right: auto;
  margin-left: auto;
}

.c-footer-inner-mobile__group {
  display: block;
  box-sizing: border-box;
}

.c-footer-inner-mobile__link {
  display: inline;
  box-sizing: border-box;
  color: #141413;
  cursor: pointer;
  text-decoration-line: underline;
  text-decoration-color: #141413;
  transition: color 0.1s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.c-footer-inner-mobile__link-icon {
  display: inline-block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 46px;
  height: 32px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
}

.c-footer-inner-mobile__nav {
  display: block;
  box-sizing: border-box;
}

.c-footer-inner-mobile__group-2 {
  display: flex;
  flex-direction: column;
  gap: 32px;
  box-sizing: border-box;
  margin-bottom: 32px;
}

.c-footer-inner-mobile__group-3 {
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-sizing: border-box;
  width: 100%;
}

.c-footer-inner-mobile__heading {
  display: block;
  box-sizing: border-box;
  margin: 0px;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 12px;
  font-weight: 700;
  line-height: 16.8px;
}

.c-footer-inner-mobile__list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-footer-inner-mobile__nav-item {
  display: list-item;
  box-sizing: border-box;
}

.c-footer-inner-mobile__nav-link {
  display: inline;
  box-sizing: border-box;
  color: #b0aea5;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 12px;
  line-height: 16.8px;
  text-decoration-line: none;
}

.c-footer-inner-mobile__link:hover {
  color: #87867f;
  text-decoration-color: #87867f;
}

.c-footer-inner-mobile__link:focus {
  color: #87867f;
  outline: none;
  text-decoration-color: #87867f;
}

.c-footer-inner-mobile__nav-link:hover {
  color: #ffffff;
  text-decoration-line: underline;
  text-decoration-color: #ffffff;
}
```

**States**

- `footer-inner-link` focus (`footer-inner-link-focus`): color #87867F, outline none, text-decoration-color #87867F
- `footer-inner-nav-link` hover (`footer-inner-nav-link-hover`): color #FFFFFF, text-decoration-line underline, text-decoration-color #FFFFFF
- mobile, `footer-inner-mobile-link` hover (`footer-inner-mobile-link-hover`): color #87867F, text-decoration-color #87867F
- mobile, `footer-inner-mobile-link` focus (`footer-inner-mobile-link-focus`): color #87867F, outline none, text-decoration-color #87867F
- mobile, `footer-inner-mobile-nav-link` hover (`footer-inner-mobile-nav-link-hover`): color #FFFFFF, text-decoration-line underline, text-decoration-color #FFFFFF

### Button, ghost (2)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `button-ghost-2`: the component root, a `<a>` (`.c-button-ghost-2`)
- `button-ghost-2-label`: label text, 8 characters (`.c-button-ghost-2__label`)
- `button-ghost-2-group`: inner flex row (`.c-button-ghost-2__group`)
- `button-ghost-2-icon`: icon placeholder, 17x16px (`.c-button-ghost-2__icon`)

**Recipe**

```html
<div class="c-button-ghost-2-scope">
  <a class="c-button-ghost-2" href="#">
    <span class="c-button-ghost-2__label">lorem ip</span>
    <span class="c-button-ghost-2__group">
      <span class="c-button-ghost-2__icon" aria-hidden="true"></span>
    </span>
  </a>
</div>
```

```css
.c-button-ghost-2-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-button-ghost-2 {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  height: 40px;
  min-width: 44px;
  padding: 8px 16px 8px 24px;
  background-color: #f5f4ed;
  color: #73726c;
  border: 1px solid #d1cfc5;
  border-radius: 8px;
  cursor: pointer;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
  text-decoration-line: none;
  transition-duration: 0.2s, 0.2s;
  transition-timing-function:
    cubic-bezier(0.77, 0, 0.175, 1), cubic-bezier(0.77, 0, 0.175, 1);
  transition-property: background-color, color;
}

.c-button-ghost-2__label {
  display: block;
  box-sizing: border-box;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  line-height: 21px;
}

.c-button-ghost-2__group {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
}

.c-button-ghost-2__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 17px;
  height: 16px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
}
```

**States**

- No hover or focus change was observed.

### Button, ghost (3)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `button-ghost-3`: the component root, a `<button>` (`.c-button-ghost-3`), 15-character label

**Recipe**

```html
<div class="c-button-ghost-3-scope">
  <button class="c-button-ghost-3" type="button">lorem ipsum dol</button>
</div>
```

```css
.c-button-ghost-3-scope {
  background-color: #141413;
  color: #faf9f5;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-button-ghost-3 {
  display: inline-block;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #b0aea5;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 12px;
  font-weight: 400;
  line-height: 16.8px;
  letter-spacing: normal;
  text-transform: none;
  text-align: start;
  list-style-type: none;
}

.c-button-ghost-3:focus {
  color: #ffffff;
  outline: none;
  text-decoration-line: underline;
  text-decoration-color: #ffffff;
}
```

**States**

- focus (`button-ghost-3-focus`): color #FFFFFF, outline none, text-decoration-line underline, text-decoration-color #FFFFFF

### Input

**Verification**: verified against the live page at desktop.

**Anatomy**

- `input`: the component root, a `<input>` (`.c-input`), 6-character placeholder

**Recipe**

```html
<div class="c-input-scope">
  <input class="c-input" type="text" placeholder="lorem" />
</div>
```

```css
.c-input-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-input {
  display: inline-block;
  border-spacing: 0px;
  box-sizing: border-box;
  width: 294px;
  height: 44px;
  min-height: 44px;
  padding: 8px 16px 8px 40px;
  overflow-x: clip;
  overflow-y: clip;
  background-color: #ffffff;
  color: #141413;
  border: 1px solid #d1cfc5;
  border-radius: 12px;
  cursor: text;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 14px;
  font-weight: 400;
  line-height: 14px;
  letter-spacing: normal;
  text-transform: none;
  text-align: start;
  transition: all 0.2s ease;
}

.c-input:focus {
  border: 1px solid #87867f;
  outline: none;
}
```

**States**

- focus: border 1px solid #87867F, outline none

### Card (3)

**Verification**: verified against the live page at desktop.

**Anatomy**

- Group: 5 instances in a 5-column grid, 32px gap; the recipe carries the values they all share
- `card-3`: the component root, a `<div>` (`.c-card-3`)
- `card-3-title`: heading, 9 characters (`.c-card-3__title`)
- `card-3-body`: label text, 143 characters (`.c-card-3__body`)

**Recipe**

```html
<div class="c-card-3-scope">
  <div class="c-card-3">
    <h3 class="c-card-3__title">lorem ips</h3>
    <p class="c-card-3__body">
      lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod
      tempor lorem ipsum dolor sit amet consectetur adipiscing elit sed do eius
    </p>
  </div>
</div>
```

```css
.c-card-3-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-card-3 {
  display: inline-flex;
  flex-direction: column;
  flex-grow: 1;
  flex-basis: 0%;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  max-width: 640px;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
}

.c-card-3__title {
  display: block;
  box-sizing: border-box;
  margin: 0px;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 19px;
  font-weight: 600;
  line-height: 22.8px;
}

.c-card-3__body {
  display: block;
  box-sizing: border-box;
  margin: 0px;
  font-size: 15px;
  line-height: 21px;
}
```

**States**

- No hover or focus change was observed.

### Footer navigation

**Verification**: flagged, the `footer-navigation` height did not reproduce the measured 975px after 2 correction attempts.

**Anatomy**

- `footer-navigation`: the component root, a `<nav>` (`.c-footer-navigation`), content not captured
- `footer-navigation-group`: inner flex column (`.c-footer-navigation__group`, 2 instances), content not captured
- `footer-navigation-group-2`: inner flex column (`.c-footer-navigation__group-2`, 3 instances)
- `footer-navigation-title`: heading, 8 characters (`.c-footer-navigation__title`, 3 instances)
- `footer-navigation-list`: inner flex column (`.c-footer-navigation__list`, 3 instances), content not captured
- `footer-navigation-item`: inner group (`.c-footer-navigation__item`, 28 instances), content not captured

**Recipe**

```html
<div class="c-footer-navigation-scope">
  <nav class="c-footer-navigation">
    <div class="c-footer-navigation__group">
      <div class="c-footer-navigation__group-2">
        <h3 class="c-footer-navigation__title">lorem ip</h3>
        <ul class="c-footer-navigation__list">
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
        </ul>
      </div>
      <div class="c-footer-navigation__group-2">
        <h3 class="c-footer-navigation__title">lorem</h3>
        <ul class="c-footer-navigation__list">
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
        </ul>
      </div>
    </div>
    <div class="c-footer-navigation__group">
      <div class="c-footer-navigation__group-2">
        <h3 class="c-footer-navigation__title">lorem ips</h3>
        <ul class="c-footer-navigation__list">
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
          <li class="c-footer-navigation__item"></li>
        </ul>
      </div>
    </div>
  </nav>
</div>
```

```css
.c-footer-navigation-scope {
  background-color: #141413;
  color: #faf9f5;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-footer-navigation {
  display: inline-grid;
  gap: 32px;
  grid-template-columns: repeat(4, 1fr);
  border-spacing: 0px;
  box-sizing: border-box;
  color: #faf9f5;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
}

.c-footer-navigation__group {
  display: flex;
  flex-direction: column;
  gap: 48px;
  box-sizing: border-box;
}

.c-footer-navigation__group-2 {
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-sizing: border-box;
  width: 100%;
}

.c-footer-navigation__title {
  display: block;
  box-sizing: border-box;
  margin: 0px;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 12px;
  font-weight: 700;
  line-height: 16.8px;
}

.c-footer-navigation__list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-footer-navigation__item {
  display: list-item;
  box-sizing: border-box;
}
```

**States**

- No hover or focus change was observed.

### Navigation menu

**Verification**: verified against the live page at desktop.

**Anatomy**

- `navigation-menu`: the component root, a `<nav>` (`.c-navigation-menu`)
- `navigation-menu-list`: inner flex row (`.c-navigation-menu__list`)
- `navigation-menu-item`: inner group (`.c-navigation-menu__item`, 5 instances)
- `navigation-menu-button`: button (`.c-navigation-menu__button`, 3 instances)
- `navigation-menu-text`: label text, 8 characters (`.c-navigation-menu__text`, 3 instances)
- `navigation-menu-icon`: icon placeholder, 12x6px (`.c-navigation-menu__icon`, 3 instances)
- `navigation-menu-link`: link, 6-character label (`.c-navigation-menu__link`, 2 instances)

**Recipe**

```html
<div class="c-navigation-menu-scope">
  <nav class="c-navigation-menu">
    <ul class="c-navigation-menu__list">
      <li class="c-navigation-menu__item">
        <button class="c-navigation-menu__button" type="button">
          <span class="c-navigation-menu__text">lorem ip</span>
          <span class="c-navigation-menu__icon" aria-hidden="true"></span>
        </button>
      </li>
      <li class="c-navigation-menu__item">
        <a class="c-navigation-menu__link" href="#">lorem</a>
      </li>
      <li class="c-navigation-menu__item">
        <button class="c-navigation-menu__button" type="button">
          <span class="c-navigation-menu__text">lorem ipsum</span>
          <span class="c-navigation-menu__icon" aria-hidden="true"></span>
        </button>
      </li>
      <li class="c-navigation-menu__item">
        <button class="c-navigation-menu__button" type="button">
          <span class="c-navigation-menu__text">lorem</span>
          <span class="c-navigation-menu__icon" aria-hidden="true"></span>
        </button>
      </li>
      <li class="c-navigation-menu__item">
        <a class="c-navigation-menu__link" href="#">lore</a>
      </li>
    </ul>
  </nav>
</div>
```

```css
.c-navigation-menu-scope {
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-navigation-menu {
  display: inline-flex;
  align-items: center;
  border-spacing: 0px;
  box-sizing: border-box;
  color: #0f0f0e;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
}

.c-navigation-menu__list {
  display: flex;
  gap: 24px;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-navigation-menu__item {
  display: list-item;
  box-sizing: border-box;
  position: relative;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  line-height: 21px;
}

.c-navigation-menu__button {
  display: flex;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
}

.c-navigation-menu__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-navigation-menu__link {
  display: flex;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  color: #0f0f0e;
  cursor: pointer;
  letter-spacing: -0.0375px;
  text-decoration-line: none;
  white-space: nowrap;
}
```

**States**

- No hover or focus change was observed.

### Navigation menu (2)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `navigation-menu-2`: the component root, a `<button>` (`.c-navigation-menu-2`)
- `navigation-menu-2-text`: label text, 8 characters (`.c-navigation-menu-2__text`)
- `navigation-menu-2-icon`: icon placeholder, 12x6px (`.c-navigation-menu-2__icon`)

**Recipe**

```html
<div class="c-navigation-menu-2-scope">
  <button class="c-navigation-menu-2" type="button">
    <span class="c-navigation-menu-2__text">lorem ip</span>
    <span class="c-navigation-menu-2__icon" aria-hidden="true"></span>
  </button>
</div>
```

```css
.c-navigation-menu-2-scope {
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
}

.c-navigation-menu-2 {
  display: flex;
  align-items: center;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
  list-style-type: none;
}

.c-navigation-menu-2__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-navigation-menu-2:hover {
  text-decoration-line: underline;
}
```

**States**

- hover: text-decoration-line underline

### Navigation menu (3)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `navigation-menu-3`: the component root, a `<button>` (`.c-navigation-menu-3`)
- `navigation-menu-3-text`: label text, 11 characters (`.c-navigation-menu-3__text`)
- `navigation-menu-3-icon`: icon placeholder, 12x6px (`.c-navigation-menu-3__icon`)

**Recipe**

```html
<div class="c-navigation-menu-3-scope">
  <button class="c-navigation-menu-3" type="button">
    <span class="c-navigation-menu-3__text">lorem ipsum</span>
    <span class="c-navigation-menu-3__icon" aria-hidden="true"></span>
  </button>
</div>
```

```css
.c-navigation-menu-3-scope {
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
}

.c-navigation-menu-3 {
  display: flex;
  align-items: center;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
  list-style-type: none;
}

.c-navigation-menu-3__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(0.984618, 0.174719, -0.174719, 0.984618, 0, 0.944098);
  transition: transform 0.2s ease-in-out;
}

.c-navigation-menu-3:hover {
  text-decoration-line: underline;
}
```

**States**

- hover: text-decoration-line underline

### Button, secondary (3)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `button-secondary-3`: the component root, a `<a>` (`.c-button-secondary-3`)
- `button-secondary-3-label`: label text, 8 characters (`.c-button-secondary-3__label`)
- `button-secondary-3-group`: inner flex row (`.c-button-secondary-3__group`)
- `button-secondary-3-icon`: icon placeholder, 17x16px (`.c-button-secondary-3__icon`)

**Recipe**

```html
<div class="c-button-secondary-3-scope">
  <a class="c-button-secondary-3" href="#">
    <span class="c-button-secondary-3__label">lorem ip</span>
    <span class="c-button-secondary-3__group">
      <span class="c-button-secondary-3__icon" aria-hidden="true"></span>
    </span>
  </a>
</div>
```

```css
.c-button-secondary-3-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-button-secondary-3 {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  height: 40px;
  min-width: 44px;
  padding: 8px 16px 8px 24px;
  background-color: #f5f4ed;
  color: #73726c;
  border: 1px solid #d1cfc5;
  border-radius: 8px;
  cursor: pointer;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
  text-decoration-line: none;
  transition-duration: 0.2s, 0.2s;
  transition-timing-function:
    cubic-bezier(0.77, 0, 0.175, 1), cubic-bezier(0.77, 0, 0.175, 1);
  transition-property: background-color, color;
}

.c-button-secondary-3__label {
  display: block;
  box-sizing: border-box;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  line-height: 21px;
}

.c-button-secondary-3__group {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
}

.c-button-secondary-3__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 17px;
  height: 16px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
}

.c-button-secondary-3:hover {
  background-color: #e8e6dc;
}
```

**States**

- hover (`button-secondary-3-hover`): background-color #E8E6DC

### Button, ghost (4)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `button-ghost-4`: the component root, a `<a>` (`.c-button-ghost-4`)
- `button-ghost-4-label`: label text, 9 characters (`.c-button-ghost-4__label`)
- `button-ghost-4-group`: inner flex row (`.c-button-ghost-4__group`)
- `button-ghost-4-icon`: icon placeholder, 20px (`.c-button-ghost-4__icon`)

**Recipe**

```html
<div class="c-button-ghost-4-scope">
  <a class="c-button-ghost-4" href="#">
    <span class="c-button-ghost-4__label">lorem ips</span>
    <span class="c-button-ghost-4__group">
      <span class="c-button-ghost-4__icon" aria-hidden="true"></span>
    </span>
  </a>
</div>
```

```css
.c-button-ghost-4-scope {
  background-color: #f0eee6;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-button-ghost-4 {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
  gap: 4px;
  border-spacing: 0px;
  box-sizing: border-box;
  width: fit-content;
  height: 28px;
  min-width: 44px;
  padding: 4px 12px 4px 8px;
  background-color: #f5f4ed;
  color: #73726c;
  border: 1px solid #d1cfc5;
  border-radius: 6px;
  cursor: pointer;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
  text-decoration-line: none;
  transition-duration: 0.2s, 0.2s;
  transition-timing-function:
    cubic-bezier(0.77, 0, 0.175, 1), cubic-bezier(0.77, 0, 0.175, 1);
  transition-property: background-color, color;
}

.c-button-ghost-4__label {
  display: block;
  box-sizing: border-box;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 14px;
  line-height: 16.8px;
  letter-spacing: 0.15px;
}

.c-button-ghost-4__group {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
}

.c-button-ghost-4__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 20px;
  height: 20px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
}

.c-button-ghost-4:hover {
  background-color: #e8e6dc;
}
```

**States**

- hover (`button-ghost-4-hover`): background-color #E8E6DC

### Footer link columns

**Verification**: flagged, the `footer-link-column` height did not reproduce the measured 975px after 2 correction attempts.

**Anatomy**

- `footer-link-column`: the component root, a `<nav>` (`.c-footer-link-column`), content not captured
- `footer-link-column-group`: inner flex column (`.c-footer-link-column__group`, 2 instances), content not captured
- `footer-link-column-group-2`: inner flex column (`.c-footer-link-column__group-2`, 3 instances)
- `footer-link-column-title`: heading, 8 characters (`.c-footer-link-column__title`, 3 instances)
- `footer-link-column-list`: inner flex column (`.c-footer-link-column__list`, 3 instances), content not captured
- `footer-link-column-item`: inner group (`.c-footer-link-column__item`, 28 instances), content not captured

**Recipe**

```html
<div class="c-footer-link-column-scope">
  <nav class="c-footer-link-column">
    <div class="c-footer-link-column__group">
      <div class="c-footer-link-column__group-2">
        <h3 class="c-footer-link-column__title">lorem ip</h3>
        <ul class="c-footer-link-column__list">
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
        </ul>
      </div>
      <div class="c-footer-link-column__group-2">
        <h3 class="c-footer-link-column__title">lorem</h3>
        <ul class="c-footer-link-column__list">
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
        </ul>
      </div>
    </div>
    <div class="c-footer-link-column__group">
      <div class="c-footer-link-column__group-2">
        <h3 class="c-footer-link-column__title">lorem ips</h3>
        <ul class="c-footer-link-column__list">
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
          <li class="c-footer-link-column__item"></li>
        </ul>
      </div>
    </div>
  </nav>
</div>
```

```css
.c-footer-link-column-scope {
  background-color: #141413;
  color: #faf9f5;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-footer-link-column {
  display: inline-grid;
  gap: 32px;
  grid-template-columns: repeat(4, 1fr);
  border-spacing: 0px;
  box-sizing: border-box;
  color: #faf9f5;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
}

.c-footer-link-column__group {
  display: flex;
  flex-direction: column;
  gap: 48px;
  box-sizing: border-box;
}

.c-footer-link-column__group-2 {
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-sizing: border-box;
  width: 100%;
}

.c-footer-link-column__title {
  display: block;
  box-sizing: border-box;
  margin: 0px;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 12px;
  font-weight: 700;
  line-height: 16.8px;
}

.c-footer-link-column__list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-footer-link-column__item {
  display: list-item;
  box-sizing: border-box;
}
```

**States**

- No hover or focus change was observed.

### Navigation dropdown

**Verification**: verified against the live page at desktop.

**Anatomy**

- `navigation-dropdown`: the component root, a `<button>` (`.c-navigation-dropdown`)
- `navigation-dropdown-text`: label text, 8 characters (`.c-navigation-dropdown__text`)
- `navigation-dropdown-icon`: icon placeholder, 12x6px (`.c-navigation-dropdown__icon`)

**Recipe**

```html
<div class="c-navigation-dropdown-scope">
  <button class="c-navigation-dropdown" type="button">
    <span class="c-navigation-dropdown__text">lorem ip</span>
    <span class="c-navigation-dropdown__icon" aria-hidden="true"></span>
  </button>
</div>
```

```css
.c-navigation-dropdown-scope {
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
}

.c-navigation-dropdown {
  display: flex;
  align-items: center;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
  list-style-type: none;
}

.c-navigation-dropdown__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-navigation-dropdown:hover {
  text-decoration-line: underline;
}
```

**States**

- hover: text-decoration-line underline

### Navigation dropdown (2)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `navigation-dropdown-2`: the component root, a `<button>` (`.c-navigation-dropdown-2`)
- `navigation-dropdown-2-text`: label text, 11 characters (`.c-navigation-dropdown-2__text`)
- `navigation-dropdown-2-icon`: icon placeholder, 12x6px (`.c-navigation-dropdown-2__icon`)

**Recipe**

```html
<div class="c-navigation-dropdown-2-scope">
  <button class="c-navigation-dropdown-2" type="button">
    <span class="c-navigation-dropdown-2__text">lorem ipsum</span>
    <span class="c-navigation-dropdown-2__icon" aria-hidden="true"></span>
  </button>
</div>
```

```css
.c-navigation-dropdown-2-scope {
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
}

.c-navigation-dropdown-2 {
  display: flex;
  align-items: center;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
  list-style-type: none;
}

.c-navigation-dropdown-2__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-navigation-dropdown-2:hover {
  text-decoration-line: underline;
}
```

**States**

- hover: text-decoration-line underline

### Navigation dropdown (3)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `navigation-dropdown-3`: the component root, a `<button>` (`.c-navigation-dropdown-3`)
- `navigation-dropdown-3-text`: label text, 5 characters (`.c-navigation-dropdown-3__text`)
- `navigation-dropdown-3-icon`: icon placeholder, 12x6px (`.c-navigation-dropdown-3__icon`)

**Recipe**

```html
<div class="c-navigation-dropdown-3-scope">
  <button class="c-navigation-dropdown-3" type="button">
    <span class="c-navigation-dropdown-3__text">lorem</span>
    <span class="c-navigation-dropdown-3__icon" aria-hidden="true"></span>
  </button>
</div>
```

```css
.c-navigation-dropdown-3-scope {
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
}

.c-navigation-dropdown-3 {
  display: flex;
  align-items: center;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
  list-style-type: none;
}

.c-navigation-dropdown-3__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-navigation-dropdown-3:hover {
  text-decoration-line: underline;
}
```

**States**

- hover: text-decoration-line underline

### Legal text

**Verification**: verified against the live page at desktop.

**Anatomy**

- `legal-text`: the component root, a `<small>` (`.c-legal-text`), 83-character placeholder

**Recipe**

```html
<div class="c-legal-text-scope">
  <small class="c-legal-text"
    >lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod
    tempor lorem</small
  >
</div>
```

```css
.c-legal-text-scope {
  background-color: #141413;
  color: #faf9f5;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-legal-text {
  display: inline-block;
  border-spacing: 0px;
  box-sizing: border-box;
  color: #b0aea5;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 12px;
  font-weight: 400;
  line-height: 16.8px;
}
```

**States**

- No hover or focus change was observed.

### Nav menu (3)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `nav-menu-3`: the component root, a `<nav>` (`.c-nav-menu-3`)
- `nav-menu-3-list`: inner flex row (`.c-nav-menu-3__list`)
- `nav-menu-3-item`: inner group (`.c-nav-menu-3__item`, 5 instances)
- `nav-menu-3-button`: button (`.c-nav-menu-3__button`, 3 instances)
- `nav-menu-3-text`: label text, 8 characters (`.c-nav-menu-3__text`, 3 instances)
- `nav-menu-3-icon`: icon placeholder, 12x6px (`.c-nav-menu-3__icon`, 3 instances)
- `nav-menu-3-link`: link, 6-character label (`.c-nav-menu-3__link`, 2 instances)

**Recipe**

```html
<div class="c-nav-menu-3-scope">
  <nav class="c-nav-menu-3">
    <ul class="c-nav-menu-3__list">
      <li class="c-nav-menu-3__item">
        <button class="c-nav-menu-3__button" type="button">
          <span class="c-nav-menu-3__text">lorem ip</span>
          <span class="c-nav-menu-3__icon" aria-hidden="true"></span>
        </button>
      </li>
      <li class="c-nav-menu-3__item">
        <a class="c-nav-menu-3__link" href="#">lorem</a>
      </li>
      <li class="c-nav-menu-3__item">
        <button class="c-nav-menu-3__button" type="button">
          <span class="c-nav-menu-3__text">lorem ipsum</span>
          <span class="c-nav-menu-3__icon" aria-hidden="true"></span>
        </button>
      </li>
      <li class="c-nav-menu-3__item">
        <button class="c-nav-menu-3__button" type="button">
          <span class="c-nav-menu-3__text">lorem</span>
          <span class="c-nav-menu-3__icon" aria-hidden="true"></span>
        </button>
      </li>
      <li class="c-nav-menu-3__item">
        <a class="c-nav-menu-3__link" href="#">lore</a>
      </li>
    </ul>
  </nav>
</div>
```

```css
.c-nav-menu-3-scope {
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-nav-menu-3 {
  display: inline-flex;
  align-items: center;
  border-spacing: 0px;
  box-sizing: border-box;
  color: #0f0f0e;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
}

.c-nav-menu-3__list {
  display: flex;
  gap: 24px;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-nav-menu-3__item {
  display: list-item;
  box-sizing: border-box;
  position: relative;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  line-height: 21px;
}

.c-nav-menu-3__button {
  display: flex;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
}

.c-nav-menu-3__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-nav-menu-3__link {
  display: flex;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  color: #0f0f0e;
  cursor: pointer;
  letter-spacing: -0.0375px;
  text-decoration-line: none;
  white-space: nowrap;
}
```

**States**

- No hover or focus change was observed.

### Header (inner, 2)

**Verification**: desktop verified against the live page at desktop; mobile verified against the live page at mobile.

Variant observed on https://www.anthropic.com/research/team/frontier-red-team.

**Anatomy**

- `header-inner-2`: the component root, a `<header>` (`.c-header-inner-2`)
- `header-inner-2-inner`: inner flex row (`.c-header-inner-2__inner`)
- `header-inner-2-logo`: link (`.c-header-inner-2__logo`)
- `header-inner-2-group`: inner flex row (`.c-header-inner-2__group`)
- `header-inner-2-group-2`: inner block (`.c-header-inner-2__group-2`)
- `header-inner-2-logo-icon`: icon placeholder, 143x16px (`.c-header-inner-2__logo-icon`)
- `header-inner-2-group-3`: inner flex row (`.c-header-inner-2__group-3`)
- `header-inner-2-nav`: inner flex row (`.c-header-inner-2__nav`)
- `header-inner-2-nav-list`: inner flex row (`.c-header-inner-2__nav-list`)
- `header-inner-2-nav-item`: inner group (`.c-header-inner-2__nav-item`, 5 instances)
- `header-inner-2-button`: button (`.c-header-inner-2__button`, 3 instances)
- `header-inner-2-text`: label text, 8 characters (`.c-header-inner-2__text`, 3 instances)
- `header-inner-2-button-icon`: icon placeholder, 12x6px (`.c-header-inner-2__button-icon`, 2 instances)
- `header-inner-2-nav-link`: link, 6-character label (`.c-header-inner-2__nav-link`, 2 instances)
- `header-inner-2-button-icon-2`: icon placeholder, 12x6px (`.c-header-inner-2__button-icon-2`)
- `header-inner-2-group-4`: inner block (`.c-header-inner-2__group-4`)
- `header-inner-2-group-5`: inner flex column (`.c-header-inner-2__group-5`)
- `header-inner-2-text-2`: label text, 11 characters (`.c-header-inner-2__text-2`, 2 instances)
- `header-inner-2-nav-list-2`: inner flex column (`.c-header-inner-2__nav-list-2`, 2 instances), content not captured
- `header-inner-2-group-6`: inner flex column (`.c-header-inner-2__group-6`)
- `header-inner-2-group-7`: inner flex row (`.c-header-inner-2__group-7`)
- `header-inner-2-cta`: the `button-primary-2` button, 10-character label (`.c-header-inner-2__cta`)
- `header-inner-2-group-8`: inner flex row (`.c-header-inner-2__group-8`)
- `header-inner-2-icon`: icon placeholder, 12x6px (`.c-header-inner-2__icon`)

**Desktop recipe**

```html
<div class="c-header-inner-2-scope">
  <header class="c-header-inner-2">
    <div class="c-header-inner-2__inner">
      <a class="c-header-inner-2__logo" href="#">
        <div class="c-header-inner-2__group">
          <div class="c-header-inner-2__group-2">
            <span class="c-header-inner-2__logo-icon" aria-hidden="true"></span>
          </div>
        </div>
      </a>
      <div class="c-header-inner-2__group-3">
        <nav class="c-header-inner-2__nav">
          <ul class="c-header-inner-2__nav-list">
            <li class="c-header-inner-2__nav-item">
              <button class="c-header-inner-2__button" type="button">
                <span class="c-header-inner-2__text">lorem ip</span>
                <span
                  class="c-header-inner-2__button-icon"
                  aria-hidden="true"
                ></span>
              </button>
            </li>
            <li class="c-header-inner-2__nav-item">
              <a class="c-header-inner-2__nav-link" href="#">lorem</a>
            </li>
            <li class="c-header-inner-2__nav-item">
              <button class="c-header-inner-2__button" type="button">
                <span class="c-header-inner-2__text">lorem ipsum</span>
                <span
                  class="c-header-inner-2__button-icon-2"
                  aria-hidden="true"
                ></span>
              </button>
              <div class="c-header-inner-2__group-4">
                <div class="c-header-inner-2__group-5">
                  <p class="c-header-inner-2__text-2">lorem ipsum</p>
                  <ul class="c-header-inner-2__nav-list-2"></ul>
                </div>
                <div class="c-header-inner-2__group-6">
                  <p class="c-header-inner-2__text-2">lorem ipsum</p>
                  <ul class="c-header-inner-2__nav-list-2"></ul>
                </div>
              </div>
            </li>
            <li class="c-header-inner-2__nav-item">
              <button class="c-header-inner-2__button" type="button">
                <span class="c-header-inner-2__text">lorem</span>
                <span
                  class="c-header-inner-2__button-icon"
                  aria-hidden="true"
                ></span>
              </button>
            </li>
            <li class="c-header-inner-2__nav-item">
              <a class="c-header-inner-2__nav-link" href="#">lore</a>
            </li>
          </ul>
        </nav>
        <div class="c-header-inner-2__group-7">
          <a class="c-header-inner-2__cta" href="#">lorem ipsu</a>
          <div class="c-header-inner-2__group-8">
            <span class="c-header-inner-2__icon" aria-hidden="true"></span>
          </div>
        </div>
      </div>
    </div>
  </header>
</div>
```

```css
.c-header-inner-2-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-header-inner-2 {
  display: block;
  border-spacing: 0px;
  box-sizing: border-box;
  position: sticky;
  top: 0px;
  z-index: 9999;
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
  padding-top: 16px;
  padding-bottom: 16px;
}

.c-header-inner-2__inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-sizing: border-box;
  width: 100%;
  max-width: 1400px;
  padding-right: 64px;
  padding-left: 64px;
  margin-right: auto;
  margin-left: auto;
}

.c-header-inner-2__logo {
  display: block;
  box-sizing: border-box;
  color: #141413;
  cursor: pointer;
  text-decoration-line: underline;
  text-decoration-color: #141413;
  transition: color 0.1s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.c-header-inner-2__group {
  display: flex;
  align-items: center;
  box-sizing: border-box;
  width: 143px;
  height: 16px;
  position: relative;
}

.c-header-inner-2__group-2 {
  display: block;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  position: relative;
}

.c-header-inner-2__logo-icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 143px;
  height: 16px;
  position: absolute;
  top: 0px;
  right: 0px;
  bottom: 0px;
  left: 0px;
  overflow-x: hidden;
  overflow-y: hidden;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 0);
}

.c-header-inner-2__group-3 {
  display: flex;
  align-items: center;
  gap: 24px;
  box-sizing: border-box;
  margin-left: auto;
}

.c-header-inner-2__nav {
  display: flex;
  align-items: center;
  box-sizing: border-box;
}

.c-header-inner-2__nav-list {
  display: flex;
  gap: 24px;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-header-inner-2__nav-item {
  display: list-item;
  box-sizing: border-box;
  position: relative;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  line-height: 21px;
}

.c-header-inner-2__button {
  display: flex;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
}

.c-header-inner-2__button-icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-header-inner-2__nav-link {
  display: flex;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  color: #0f0f0e;
  cursor: pointer;
  letter-spacing: -0.0375px;
  text-decoration-line: none;
  white-space: nowrap;
}

.c-header-inner-2__button-icon-2 {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(-1, 0, 0, -1, 0, 0);
  transition: transform 0.2s ease-in-out;
}

.c-header-inner-2__group-4 {
  display: block;
  box-sizing: border-box;
  min-width: 250px;
  padding: 24px;
  position: absolute;
  top: calc(100% + 1px);
  left: 50%;
  z-index: 100;
  background-color: #faf9f5;
  border: 1px solid #f0eee6;
  border-radius: 16px;
  box-shadow:
    #00000003 0px 2px 2px 0px,
    #00000005 0px 4px 4px 0px,
    #0000000a 0px 16px 24px 0px;
  opacity: 0.999893;
  transform: matrix(1, 0, 0, 1, -125, 0);
  margin-top: 8px;
}

.c-header-inner-2__group-5 {
  display: flex;
  flex-direction: column;
  gap: 8px;
  box-sizing: border-box;
  padding-bottom: 16px;
  margin-bottom: 16px;
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: #e8e6dc;
}

.c-header-inner-2__text-2 {
  display: block;
  box-sizing: border-box;
  margin: 0px;
  color: #5e5d59;
  font-size: 14px;
  line-height: 16.8px;
  letter-spacing: 0.15px;
}

.c-header-inner-2__nav-list-2 {
  display: flex;
  flex-direction: column;
  gap: 8px;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-header-inner-2__group-6 {
  display: flex;
  flex-direction: column;
  gap: 8px;
  box-sizing: border-box;
}

.c-header-inner-2__group-7 {
  display: flex;
  box-sizing: border-box;
  position: relative;
}

.c-header-inner-2__cta {
  display: block;
  box-sizing: border-box;
  height: 36px;
  padding: 8px 16px;
  background-color: #0f0f0e;
  color: #faf9f5;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  line-height: 21px;
  text-decoration-line: none;
  transition: background-color 0.2s ease;
  border-top-left-radius: 8px;
  border-bottom-left-radius: 8px;
}

.c-header-inner-2__group-8 {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  padding: 12px 16px;
  position: relative;
  background-color: #0f0f0e;
  color: #faf9f5;
  cursor: pointer;
  transition: background-color 0.2s ease;
  border-left-width: 1px;
  border-left-style: solid;
  border-left-color: #ffffff33;
  border-top-right-radius: 8px;
  border-bottom-right-radius: 8px;
}

.c-header-inner-2__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transition: transform 0.2s ease-in-out;
}

.c-header-inner-2__logo:hover {
  color: #87867f;
  text-decoration-color: #87867f;
}

.c-header-inner-2__logo:focus {
  color: #87867f;
  outline: none;
  text-decoration-color: #87867f;
}

.c-header-inner-2__button:hover {
  text-decoration-line: underline;
}

.c-header-inner-2__nav-link:hover {
  text-decoration-line: underline;
}

.c-header-inner-2__cta:hover {
  background-color: #000000cc;
}
```

**Mobile anatomy**

- `header-inner-2-mobile`: the component root, a `<header>` (`.c-header-inner-2-mobile`)
- `header-inner-2-mobile-inner`: inner flex row (`.c-header-inner-2-mobile__inner`)
- `header-inner-2-mobile-logo`: link (`.c-header-inner-2-mobile__logo`)
- `header-inner-2-mobile-logo-icon`: icon placeholder, 32px (`.c-header-inner-2-mobile__logo-icon`)
- `header-inner-2-mobile-group`: inner flex row (`.c-header-inner-2-mobile__group`)
- `header-inner-2-mobile-menu-toggle`: button (`.c-header-inner-2-mobile__menu-toggle`)
- `header-inner-2-mobile-menu-toggle-icon`: icon placeholder, 24px (`.c-header-inner-2-mobile__menu-toggle-icon`)

**Mobile recipe**

```html
<div class="c-header-inner-2-mobile-scope">
  <header class="c-header-inner-2-mobile">
    <div class="c-header-inner-2-mobile__inner">
      <a class="c-header-inner-2-mobile__logo" href="#">
        <span
          class="c-header-inner-2-mobile__logo-icon"
          aria-hidden="true"
        ></span>
      </a>
      <div class="c-header-inner-2-mobile__group">
        <button class="c-header-inner-2-mobile__menu-toggle" type="button">
          <span
            class="c-header-inner-2-mobile__menu-toggle-icon"
            aria-hidden="true"
          ></span>
        </button>
      </div>
    </div>
  </header>
</div>
```

```css
.c-header-inner-2-mobile-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-header-inner-2-mobile {
  display: block;
  border-spacing: 0px;
  box-sizing: border-box;
  position: sticky;
  top: 0px;
  z-index: 9999;
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
  padding-top: 16px;
  padding-bottom: 16px;
}

.c-header-inner-2-mobile__inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-sizing: border-box;
  width: 100%;
  max-width: 1400px;
  padding-right: 32px;
  padding-left: 32px;
  margin-right: auto;
  margin-left: auto;
}

.c-header-inner-2-mobile__logo {
  display: block;
  box-sizing: border-box;
  color: #141413;
  cursor: pointer;
  text-decoration-line: underline;
  text-decoration-color: #141413;
  transition: color 0.1s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.c-header-inner-2-mobile__logo-icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 32px;
  height: 32px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
}

.c-header-inner-2-mobile__group {
  display: flex;
  align-items: center;
  gap: 24px;
  box-sizing: border-box;
  margin-left: auto;
}

.c-header-inner-2-mobile__menu-toggle {
  display: flex;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #141413;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: normal;
  text-transform: none;
  text-align: center;
}

.c-header-inner-2-mobile__menu-toggle-icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 24px;
  height: 24px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
}

.c-header-inner-2-mobile__logo:hover {
  color: #87867f;
  text-decoration-color: #87867f;
}

.c-header-inner-2-mobile__logo:focus {
  color: #87867f;
  outline: none;
  text-decoration-color: #87867f;
}
```

**States**

- `header-inner-2-logo` hover (`header-inner-2-logo-hover`): color #87867F, text-decoration-color #87867F
- `header-inner-2-logo` focus (`header-inner-2-logo-focus`): color #87867F, outline none, text-decoration-color #87867F
- `header-inner-2-button` hover: text-decoration-line underline
- `header-inner-2-nav-link` hover: text-decoration-line underline
- `header-inner-2-cta` hover (`header-inner-2-cta-hover`): background-color #000000CC
- mobile, `header-inner-2-mobile-logo` hover (`header-inner-2-mobile-logo-hover`): color #87867F, text-decoration-color #87867F
- mobile, `header-inner-2-mobile-logo` focus (`header-inner-2-mobile-logo-focus`): color #87867F, outline none, text-decoration-color #87867F

### Button, ghost (5)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `button-ghost-5`: the component root, a `<button>` (`.c-button-ghost-5`)
- `button-ghost-5-label`: label text, 8 characters (`.c-button-ghost-5__label`)
- `button-ghost-5-icon`: icon placeholder, 12x6px (`.c-button-ghost-5__icon`)

**Recipe**

```html
<div class="c-button-ghost-5-scope">
  <button class="c-button-ghost-5" type="button">
    <span class="c-button-ghost-5__label">lorem ip</span>
    <span class="c-button-ghost-5__icon" aria-hidden="true"></span>
  </button>
</div>
```

```css
.c-button-ghost-5-scope {
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
}

.c-button-ghost-5 {
  display: flex;
  align-items: center;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
  list-style-type: none;
}

.c-button-ghost-5__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-button-ghost-5:hover {
  text-decoration-line: underline;
}
```

**States**

- hover: text-decoration-line underline

### Button, ghost (6)

**Verification**: verified against the live page at desktop.

**Anatomy**

- `button-ghost-6`: the component root, a `<button>` (`.c-button-ghost-6`)
- `button-ghost-6-label`: label text, 11 characters (`.c-button-ghost-6__label`)
- `button-ghost-6-icon`: icon placeholder, 12x6px (`.c-button-ghost-6__icon`)

**Recipe**

```html
<div class="c-button-ghost-6-scope">
  <button class="c-button-ghost-6" type="button">
    <span class="c-button-ghost-6__label">lorem ipsum</span>
    <span class="c-button-ghost-6__icon" aria-hidden="true"></span>
  </button>
</div>
```

```css
.c-button-ghost-6-scope {
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
}

.c-button-ghost-6 {
  display: flex;
  align-items: center;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
  list-style-type: none;
}

.c-button-ghost-6__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-button-ghost-6:hover {
  text-decoration-line: underline;
}
```

**States**

- hover: text-decoration-line underline

### Card (4)

**Verification**: verified against the live page at desktop.

**Anatomy**

- Group: 4 instances in a 1-column grid, 16px gap; the recipe carries the values they all share
- `card-4`: the component root, a `<a>` (`.c-card-4`)
- `card-4-group`: inner flex row (`.c-card-4__group`)
- `card-4-text`: label text, 16 characters (`.c-card-4__text`)
- `card-4-text-2`: label text, 11 characters (`.c-card-4__text-2`)
- `card-4-title`: heading, 66 characters (`.c-card-4__title`)
- `card-4-body`: label text, 140 characters (`.c-card-4__body`)

**Recipe**

```html
<div class="c-card-4-scope">
  <a class="c-card-4" href="#">
    <div class="c-card-4__group">
      <span class="c-card-4__text">lorem ipsum dolo</span>
      <time class="c-card-4__text-2">lorem ipsum</time>
    </div>
    <h4 class="c-card-4__title">
      lorem ipsum dolor sit amet consectetur adipiscing elit sed do eius
    </h4>
    <p class="c-card-4__body">
      lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod
      tempor lorem ipsum dolor sit amet consectetur adipiscing elit sed do e
    </p>
  </a>
</div>
```

```css
.c-card-4-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-card-4 {
  display: inline-flex;
  flex-direction: column;
  gap: 8px;
  border-spacing: 0px;
  box-sizing: border-box;
  color: #141413;
  cursor: pointer;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
  text-decoration-line: none;
}

.c-card-4__group {
  display: flex;
  gap: 8px;
  box-sizing: border-box;
}

.c-card-4__text {
  display: block;
  box-sizing: border-box;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 14px;
  font-weight: 500;
  line-height: 16.8px;
  letter-spacing: 0.15px;
}

.c-card-4__text-2 {
  display: block;
  box-sizing: border-box;
  color: #5e5d59;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 14px;
  font-weight: 500;
  line-height: 16.8px;
  letter-spacing: 0.15px;
}

.c-card-4__title {
  display: block;
  box-sizing: border-box;
  max-width: 640px;
  margin: 0px;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 19px;
  font-weight: 600;
  line-height: 22.8px;
}

.c-card-4__body {
  display: block;
  box-sizing: border-box;
  max-width: 640px;
  margin: 0px;
  font-size: 15px;
  line-height: 21px;
}

.c-card-4:hover {
  padding: 0px 0px 16px;
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: #d1cfc5;
}

.c-card-4:focus {
  padding: 0px 0px 16px;
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: #d1cfc5;
}
```

**States**

- hover: padding 0px 0px 16px, border-bottom-width 1px, border-bottom-style solid, border-bottom-color #D1CFC5
- focus: padding 0px 0px 16px, border-bottom-width 1px, border-bottom-style solid, border-bottom-color #D1CFC5

### Nav

**Verification**: verified against the live page at desktop.

**Anatomy**

- `nav`: the component root, a `<nav>` (`.c-nav`)
- `nav-list`: inner flex row (`.c-nav__list`)
- `nav-item`: inner group (`.c-nav__item`, 5 instances)
- `nav-button`: button (`.c-nav__button`, 3 instances)
- `nav-text`: label text, 8 characters (`.c-nav__text`, 3 instances)
- `nav-icon`: icon placeholder, 12x6px (`.c-nav__icon`, 3 instances)
- `nav-link`: link, 6-character label (`.c-nav__link`, 2 instances)

**Recipe**

```html
<div class="c-nav-scope">
  <nav class="c-nav">
    <ul class="c-nav__list">
      <li class="c-nav__item">
        <button class="c-nav__button" type="button">
          <span class="c-nav__text">lorem ip</span>
          <span class="c-nav__icon" aria-hidden="true"></span>
        </button>
      </li>
      <li class="c-nav__item">
        <a class="c-nav__link" href="#">lorem</a>
      </li>
      <li class="c-nav__item">
        <button class="c-nav__button" type="button">
          <span class="c-nav__text">lorem ipsum</span>
          <span class="c-nav__icon" aria-hidden="true"></span>
        </button>
      </li>
      <li class="c-nav__item">
        <button class="c-nav__button" type="button">
          <span class="c-nav__text">lorem</span>
          <span class="c-nav__icon" aria-hidden="true"></span>
        </button>
      </li>
      <li class="c-nav__item">
        <a class="c-nav__link" href="#">lore</a>
      </li>
    </ul>
  </nav>
</div>
```

```css
.c-nav-scope {
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-nav {
  display: inline-flex;
  align-items: center;
  border-spacing: 0px;
  box-sizing: border-box;
  color: #0f0f0e;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
}

.c-nav__list {
  display: flex;
  gap: 24px;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-nav__item {
  display: list-item;
  box-sizing: border-box;
  position: relative;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  line-height: 21px;
}

.c-nav__button {
  display: flex;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
}

.c-nav__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-nav__link {
  display: flex;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  color: #0f0f0e;
  cursor: pointer;
  letter-spacing: -0.0375px;
  text-decoration-line: none;
  white-space: nowrap;
}
```

**States**

- No hover or focus change was observed.

### Nav (2)

**Verification**: flagged, the `nav-2` height did not reproduce the measured 975px after 2 correction attempts.

**Anatomy**

- `nav-2`: the component root, a `<nav>` (`.c-nav-2`), content not captured
- `nav-2-group`: inner flex column (`.c-nav-2__group`, 2 instances), content not captured
- `nav-2-group-2`: inner flex column (`.c-nav-2__group-2`, 3 instances)
- `nav-2-title`: heading, 8 characters (`.c-nav-2__title`, 3 instances)
- `nav-2-list`: inner flex column (`.c-nav-2__list`, 3 instances), content not captured
- `nav-2-item`: inner group (`.c-nav-2__item`, 28 instances), content not captured

**Recipe**

```html
<div class="c-nav-2-scope">
  <nav class="c-nav-2">
    <div class="c-nav-2__group">
      <div class="c-nav-2__group-2">
        <h3 class="c-nav-2__title">lorem ip</h3>
        <ul class="c-nav-2__list">
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
        </ul>
      </div>
      <div class="c-nav-2__group-2">
        <h3 class="c-nav-2__title">lorem</h3>
        <ul class="c-nav-2__list">
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
        </ul>
      </div>
    </div>
    <div class="c-nav-2__group">
      <div class="c-nav-2__group-2">
        <h3 class="c-nav-2__title">lorem ips</h3>
        <ul class="c-nav-2__list">
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
          <li class="c-nav-2__item"></li>
        </ul>
      </div>
    </div>
  </nav>
</div>
```

```css
.c-nav-2-scope {
  background-color: #141413;
  color: #faf9f5;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-nav-2 {
  display: inline-grid;
  gap: 32px;
  grid-template-columns: repeat(4, 1fr);
  border-spacing: 0px;
  box-sizing: border-box;
  color: #faf9f5;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
}

.c-nav-2__group {
  display: flex;
  flex-direction: column;
  gap: 48px;
  box-sizing: border-box;
}

.c-nav-2__group-2 {
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-sizing: border-box;
  width: 100%;
}

.c-nav-2__title {
  display: block;
  box-sizing: border-box;
  margin: 0px;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 12px;
  font-weight: 700;
  line-height: 16.8px;
}

.c-nav-2__list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-nav-2__item {
  display: list-item;
  box-sizing: border-box;
}
```

**States**

- No hover or focus change was observed.

### Video

**Verification**: flagged, the render matched 46% of the original pixels, below the 96% required after 2 correction attempts.

**Anatomy**

- `video`: the component root, a `<button>` (`.c-video`)
- `video-media`: image placeholder, 636x358px (`.c-video__media`)
- `video-group`: inner flex row (`.c-video__group`)
- `video-icon`: icon placeholder, 22px (`.c-video__icon`)

**Recipe**

```html
<div class="c-video-scope">
  <button class="c-video" type="button">
    <span class="c-video__media" aria-hidden="true"></span>
    <div class="c-video__group">
      <span class="c-video__icon" aria-hidden="true"></span>
    </div>
  </button>
</div>
```

```css
.c-video-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-video {
  display: block;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 0px;
  position: relative;
  overflow-x: hidden;
  overflow-y: hidden;
  background-color: transparent;
  color: #000000;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: normal;
  text-transform: none;
  text-align: center;
  transition: all 0.2s ease;
}

.c-video__media {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 636px;
  height: 358px;
  max-width: 100%;
  aspect-ratio: auto 1440 / 810;
  overflow-x: clip;
  overflow-y: clip;
  vertical-align: middle;
  background-color: currentcolor;
}

.c-video__group {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  padding: 16px;
  position: absolute;
  top: 50%;
  left: 50%;
  background-color: #0f0f0e;
  color: #ffffff;
  border: 1px solid #0f0f0e;
  border-radius: 16px;
  box-shadow: #0000000d 0px 4px 24px 0px;
  transform: matrix(1, 0, 0, 1, -28, -28);
  transition-duration: 0.2s, 0.2s;
  transition-timing-function: ease, ease;
  transition-property: background, color;
}

.c-video__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 22px;
  height: 22px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
}
```

**States**

- No hover or focus change was observed.

### Video (2)

**Verification**: flagged, the render matched 54% of the original pixels, below the 96% required after 2 correction attempts.

**Anatomy**

- `video-2`: the component root, a `<button>` (`.c-video-2`)
- `video-2-media`: image placeholder, 837x471px (`.c-video-2__media`)
- `video-2-group`: inner flex row (`.c-video-2__group`)
- `video-2-icon`: icon placeholder, 22px (`.c-video-2__icon`)

**Recipe**

```html
<div class="c-video-2-scope">
  <button class="c-video-2" type="button">
    <span class="c-video-2__media" aria-hidden="true"></span>
    <div class="c-video-2__group">
      <span class="c-video-2__icon" aria-hidden="true"></span>
    </div>
  </button>
</div>
```

```css
.c-video-2-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-video-2 {
  display: block;
  border-spacing: 0px;
  box-sizing: border-box;
  padding: 0px;
  position: relative;
  overflow-x: hidden;
  overflow-y: hidden;
  background-color: transparent;
  color: #000000;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: normal;
  text-transform: none;
  text-align: center;
  transition: all 0.2s ease;
}

.c-video-2__media {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 837px;
  height: 471px;
  max-width: 100%;
  aspect-ratio: auto 1280 / 720;
  overflow-x: clip;
  overflow-y: clip;
  vertical-align: middle;
  background-color: currentcolor;
}

.c-video-2__group {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  padding: 16px;
  position: absolute;
  top: 50%;
  left: 50%;
  background-color: #0f0f0e;
  color: #ffffff;
  border: 1px solid #0f0f0e;
  border-radius: 16px;
  box-shadow: #0000000d 0px 4px 24px 0px;
  transform: matrix(1, 0, 0, 1, -28, -28);
  transition-duration: 0.2s, 0.2s;
  transition-timing-function: ease, ease;
  transition-property: background, color;
}

.c-video-2__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 22px;
  height: 22px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
}
```

**States**

- No hover or focus change was observed.

### Header (inner, 3)

**Verification**: desktop verified against the live page at desktop; mobile verified against the live page at mobile.

Variant observed on https://www.anthropic.com/research/team/interpretability.

**Anatomy**

- `header-inner-3`: the component root, a `<header>` (`.c-header-inner-3`)
- `header-inner-3-inner`: inner flex row (`.c-header-inner-3__inner`)
- `header-inner-3-logo`: link (`.c-header-inner-3__logo`)
- `header-inner-3-group`: inner flex row (`.c-header-inner-3__group`)
- `header-inner-3-group-2`: inner block (`.c-header-inner-3__group-2`)
- `header-inner-3-logo-icon`: icon placeholder, 143x16px (`.c-header-inner-3__logo-icon`)
- `header-inner-3-group-3`: inner flex row (`.c-header-inner-3__group-3`)
- `header-inner-3-nav`: inner flex row (`.c-header-inner-3__nav`)
- `header-inner-3-nav-list`: inner flex row (`.c-header-inner-3__nav-list`)
- `header-inner-3-nav-item`: inner group (`.c-header-inner-3__nav-item`, 5 instances)
- `header-inner-3-cta`: the `button-ghost-5` button (`.c-header-inner-3__cta`, 2 instances)
- `header-inner-3-text`: label text, 8 characters (`.c-header-inner-3__text`, 3 instances)
- `header-inner-3-cta-icon`: icon placeholder, 12x6px (`.c-header-inner-3__cta-icon`, 2 instances)
- `header-inner-3-nav-link`: link, 6-character label (`.c-header-inner-3__nav-link`, 2 instances)
- `header-inner-3-button`: button (`.c-header-inner-3__button`)
- `header-inner-3-button-icon`: icon placeholder, 12x6px (`.c-header-inner-3__button-icon`)
- `header-inner-3-group-4`: inner flex row (`.c-header-inner-3__group-4`)
- `header-inner-3-cta-2`: the `button-primary-2` button, 10-character label (`.c-header-inner-3__cta-2`)
- `header-inner-3-group-5`: inner flex row (`.c-header-inner-3__group-5`)
- `header-inner-3-icon`: icon placeholder, 12x6px (`.c-header-inner-3__icon`)

**Desktop recipe**

```html
<div class="c-header-inner-3-scope">
  <header class="c-header-inner-3">
    <div class="c-header-inner-3__inner">
      <a class="c-header-inner-3__logo" href="#">
        <div class="c-header-inner-3__group">
          <div class="c-header-inner-3__group-2">
            <span class="c-header-inner-3__logo-icon" aria-hidden="true"></span>
          </div>
        </div>
      </a>
      <div class="c-header-inner-3__group-3">
        <nav class="c-header-inner-3__nav">
          <ul class="c-header-inner-3__nav-list">
            <li class="c-header-inner-3__nav-item">
              <button class="c-header-inner-3__cta" type="button">
                <span class="c-header-inner-3__text">lorem ip</span>
                <span
                  class="c-header-inner-3__cta-icon"
                  aria-hidden="true"
                ></span>
              </button>
            </li>
            <li class="c-header-inner-3__nav-item">
              <a class="c-header-inner-3__nav-link" href="#">lorem</a>
            </li>
            <li class="c-header-inner-3__nav-item">
              <button class="c-header-inner-3__cta" type="button">
                <span class="c-header-inner-3__text">lorem ipsum</span>
                <span
                  class="c-header-inner-3__cta-icon"
                  aria-hidden="true"
                ></span>
              </button>
            </li>
            <li class="c-header-inner-3__nav-item">
              <button class="c-header-inner-3__button" type="button">
                <span class="c-header-inner-3__text">lorem</span>
                <span
                  class="c-header-inner-3__button-icon"
                  aria-hidden="true"
                ></span>
              </button>
            </li>
            <li class="c-header-inner-3__nav-item">
              <a class="c-header-inner-3__nav-link" href="#">lore</a>
            </li>
          </ul>
        </nav>
        <div class="c-header-inner-3__group-4">
          <a class="c-header-inner-3__cta-2" href="#">lorem ipsu</a>
          <div class="c-header-inner-3__group-5">
            <span class="c-header-inner-3__icon" aria-hidden="true"></span>
          </div>
        </div>
      </div>
    </div>
  </header>
</div>
```

```css
.c-header-inner-3-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-header-inner-3 {
  display: block;
  border-spacing: 0px;
  box-sizing: border-box;
  position: sticky;
  top: 0px;
  z-index: 9999;
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
  padding-top: 16px;
  padding-bottom: 16px;
}

.c-header-inner-3__inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-sizing: border-box;
  width: 100%;
  max-width: 1400px;
  padding-right: 64px;
  padding-left: 64px;
  margin-right: auto;
  margin-left: auto;
}

.c-header-inner-3__logo {
  display: block;
  box-sizing: border-box;
  color: #141413;
  cursor: pointer;
  text-decoration-line: underline;
  text-decoration-color: #141413;
  transition: color 0.1s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.c-header-inner-3__group {
  display: flex;
  align-items: center;
  box-sizing: border-box;
  width: 143px;
  height: 16px;
  position: relative;
}

.c-header-inner-3__group-2 {
  display: block;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  position: relative;
}

.c-header-inner-3__logo-icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 143px;
  height: 16px;
  position: absolute;
  top: 0px;
  right: 0px;
  bottom: 0px;
  left: 0px;
  overflow-x: hidden;
  overflow-y: hidden;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 0);
}

.c-header-inner-3__group-3 {
  display: flex;
  align-items: center;
  gap: 24px;
  box-sizing: border-box;
  margin-left: auto;
}

.c-header-inner-3__nav {
  display: flex;
  align-items: center;
  box-sizing: border-box;
}

.c-header-inner-3__nav-list {
  display: flex;
  gap: 24px;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.c-header-inner-3__nav-item {
  display: list-item;
  box-sizing: border-box;
  position: relative;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  line-height: 21px;
}

.c-header-inner-3__cta {
  display: flex;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
}

.c-header-inner-3__cta-icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-header-inner-3__nav-link {
  display: flex;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  color: #0f0f0e;
  cursor: pointer;
  letter-spacing: -0.0375px;
  text-decoration-line: none;
  white-space: nowrap;
}

.c-header-inner-3__button {
  display: flex;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #0f0f0e;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  font-weight: 400;
  line-height: 21px;
  letter-spacing: -0.0375px;
  text-transform: none;
  text-align: center;
  white-space: nowrap;
}

.c-header-inner-3__button-icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transform: matrix(1, 0, 0, 1, 0, 1);
  transition: transform 0.2s ease-in-out;
}

.c-header-inner-3__group-4 {
  display: flex;
  box-sizing: border-box;
  position: relative;
}

.c-header-inner-3__cta-2 {
  display: block;
  box-sizing: border-box;
  height: 36px;
  padding: 8px 16px;
  background-color: #0f0f0e;
  color: #faf9f5;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 15px;
  line-height: 21px;
  text-decoration-line: none;
  transition: background-color 0.2s ease;
  border-top-left-radius: 8px;
  border-bottom-left-radius: 8px;
}

.c-header-inner-3__group-5 {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  padding: 12px 16px;
  position: relative;
  background-color: #0f0f0e;
  color: #faf9f5;
  cursor: pointer;
  transition: background-color 0.2s ease;
  border-left-width: 1px;
  border-left-style: solid;
  border-left-color: #ffffff33;
  border-top-right-radius: 8px;
  border-bottom-right-radius: 8px;
}

.c-header-inner-3__icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 12px;
  height: 6px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
  transition: transform 0.2s ease-in-out;
}

.c-header-inner-3__logo:hover {
  color: #87867f;
  text-decoration-color: #87867f;
}

.c-header-inner-3__logo:focus {
  color: #87867f;
  outline: none;
  text-decoration-color: #87867f;
}

.c-header-inner-3__cta:hover {
  text-decoration-line: underline;
}

.c-header-inner-3__nav-link:hover {
  text-decoration-line: underline;
}

.c-header-inner-3__button:hover {
  text-decoration-line: underline;
}

.c-header-inner-3__cta-2:hover {
  background-color: #000000cc;
}
```

**Mobile anatomy**

- `header-inner-3-mobile`: the component root, a `<header>` (`.c-header-inner-3-mobile`)
- `header-inner-3-mobile-inner`: inner flex row (`.c-header-inner-3-mobile__inner`)
- `header-inner-3-mobile-logo`: link (`.c-header-inner-3-mobile__logo`)
- `header-inner-3-mobile-logo-icon`: icon placeholder, 32px (`.c-header-inner-3-mobile__logo-icon`)
- `header-inner-3-mobile-group`: inner flex row (`.c-header-inner-3-mobile__group`)
- `header-inner-3-mobile-menu-toggle`: button (`.c-header-inner-3-mobile__menu-toggle`)
- `header-inner-3-mobile-menu-toggle-icon`: icon placeholder, 24px (`.c-header-inner-3-mobile__menu-toggle-icon`)

**Mobile recipe**

```html
<div class="c-header-inner-3-mobile-scope">
  <header class="c-header-inner-3-mobile">
    <div class="c-header-inner-3-mobile__inner">
      <a class="c-header-inner-3-mobile__logo" href="#">
        <span
          class="c-header-inner-3-mobile__logo-icon"
          aria-hidden="true"
        ></span>
      </a>
      <div class="c-header-inner-3-mobile__group">
        <button class="c-header-inner-3-mobile__menu-toggle" type="button">
          <span
            class="c-header-inner-3-mobile__menu-toggle-icon"
            aria-hidden="true"
          ></span>
        </button>
      </div>
    </div>
  </header>
</div>
```

```css
.c-header-inner-3-mobile-scope {
  background-color: #faf9f5;
  color: #141413;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
}

.c-header-inner-3-mobile {
  display: block;
  border-spacing: 0px;
  box-sizing: border-box;
  position: sticky;
  top: 0px;
  z-index: 9999;
  background-color: #faf9f5;
  color: #0f0f0e;
  font-family: anthropicSerif, "anthropicSerif Fallback", serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: -0.16px;
  padding-top: 16px;
  padding-bottom: 16px;
}

.c-header-inner-3-mobile__inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-sizing: border-box;
  width: 100%;
  max-width: 1400px;
  padding-right: 32px;
  padding-left: 32px;
  margin-right: auto;
  margin-left: auto;
}

.c-header-inner-3-mobile__logo {
  display: block;
  box-sizing: border-box;
  color: #141413;
  cursor: pointer;
  text-decoration-line: underline;
  text-decoration-color: #141413;
  transition: color 0.1s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.c-header-inner-3-mobile__logo-icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 32px;
  height: 32px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
}

.c-header-inner-3-mobile__group {
  display: flex;
  align-items: center;
  gap: 24px;
  box-sizing: border-box;
  margin-left: auto;
}

.c-header-inner-3-mobile__menu-toggle {
  display: flex;
  box-sizing: border-box;
  padding: 0px;
  background-color: transparent;
  color: #141413;
  border: 0;
  cursor: pointer;
  font-family: anthropicSans, "anthropicSans Fallback", sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: normal;
  text-transform: none;
  text-align: center;
}

.c-header-inner-3-mobile__menu-toggle-icon {
  display: block;
  flex-shrink: 0;
  box-sizing: border-box;
  width: 24px;
  height: 24px;
  overflow-x: hidden;
  overflow-y: hidden;
  vertical-align: middle;
  background-color: currentcolor;
}

.c-header-inner-3-mobile__logo:focus {
  color: #87867f;
  outline: none;
  text-decoration-color: #87867f;
}
```

**States**

- `header-inner-3-logo` hover (`header-inner-3-logo-hover`): color #87867F, text-decoration-color #87867F
- `header-inner-3-logo` focus (`header-inner-3-logo-focus`): color #87867F, outline none, text-decoration-color #87867F
- `header-inner-3-cta` hover: text-decoration-line underline
- `header-inner-3-nav-link` hover: text-decoration-line underline
- `header-inner-3-button` hover: text-decoration-line underline
- `header-inner-3-cta-2` hover (`header-inner-3-cta-2-hover`): background-color #000000CC
- mobile, `header-inner-3-mobile-logo` focus (`header-inner-3-mobile-logo-focus`): color #87867F, outline none, text-decoration-color #87867F

## Do's and Don'ts

### Do

- **Reserve the ink fill for primary actions.** Use a solid `primary` (#141413) fill with `on-primary` text, as on `button-primary-3`; in the measured recipes that fill appears only on the primary CTA. On hover, step it to `surface-dark-raised` (#3D3D3A).
- **Keep standard buttons at `rounded.sm`.** `button-primary-3`, `button-secondary`, `button-ghost-2` and `button-secondary-3` all use 8px; only the compact `button-ghost-4` drops to `rounded.xs`.
- **Match the measured control heights.**
  - 40px for standard buttons (`button-primary-3`, `button-secondary`, `button-secondary-3`, `button-ghost-2`).
  - 44px for `input`.
  - 28px for the compact `button-ghost-4`.
  - 21px for text-only nav triggers (`button-ghost-5`, `button-ghost-6`).
- **Snap spacing to `base`.** Separate sections with `section-padding-y`. Place card grids on `card-3-grid-gap`; the `card-3` instances sit in a 5-column row.
- **Cap headers at `header-inner-inner-max-width`.** Desktop headers stand 68px (`header-inner`) and mobile headers 64px (`header-inner-mobile`).
- **Use only the two observed shadow tiers, and only on floating layers.** The layered `#00000003 0px 2px 2px 0px, #00000005 0px 4px 4px 0px, #0000000A 0px 16px 24px 0px` goes on panels; the soft `#0000000D 0px 4px 24px 0px` goes on media controls.
- **Keep the type roles split.** Set reading copy in Anthropic Serif (`body`, `body-lg`) and set titles in Anthropic Sans at 600 (`headline`, `title-md`).
- **On the ink footer, use the dark text pair.** Use `on-dark` for headings and `on-dark-muted` for links, brightening to white on hover as `footer-inner-nav-link` does.

### Don't

- Don't introduce a chromatic brand accent. The palette is `ink` plus warm greys, and `focus-ring` is the only blue.
- Don't use gradients; no surface on the site carries one.
- Don't box list content. Separate rows with a 1px `hairline` or #87867F bottom rule, as `card-2` and `card-4` do.
- Don't use pill or circular shapes; the largest radius is `rounded.xl` and it belongs to media.
- Don't set headlines in the serif, except the single `hero-display` statement at weight 400.
- Don't track headlines. Letter-spacing lives only on `nav-link` (-0.16px), `button` and `label` (0.15px).
- Don't use `black` (#000000) for text on parchment; `ink` is the system black.
- Don't add backdrop blur or translucency to headers; they are opaque `surface` or `surface-alt`.

## Responsive Behavior

### Two-viewport analysis

This analysis compares one desktop capture with one mobile capture. No intermediate breakpoints were observed, so none are specified here.

### Header

- **Desktop.** The header (`header-inner`) stands 68px and shows a 143px-wide wordmark (`header-inner-logo-icon`), sans nav triggers with 12×6px chevrons, and the ink CTA `button-primary-2`.
- **Mobile.** The header (`header-inner-mobile`) drops to 64px. The wordmark collapses to a 32px symbol (`header-inner-mobile-logo-icon`), and all nav moves behind a 24px hamburger (`header-inner-mobile-menu-toggle`).
- **Constant.** The 24px gap between header groups holds at both sizes (`header-inner-gap`, `header-inner-mobile-gap`).

### Content

Everything collapses to a single column on mobile:

- The split hero stacks headline above intro.
- Release cards and team-summary cards stack full width.
- List rows stack title above category.

### Footer

- The multi-column ink footer becomes one long stacked directory on mobile.
- Its inner padding drops from 64px on desktop (`footer-inner-columns`, part of `footer-inner`, flagged: the `footer-inner` height did not reproduce the measured 1103px after 2 correction attempts) to 32px (`footer-inner-mobile-inner`, part of `footer-inner-mobile`, flagged: the `footer-inner-mobile-inner` height did not reproduce the measured 3651px after 2 correction attempts).

### Touch targets

- Standard buttons are 40px tall (`button-primary-3`, `button-secondary`) and the `input` is 44px.
- The mobile menu toggle's measured size is 24px. Give it extra hit area on rebuild.
- Footer links are only 17px tall (`footer-inner-mobile-nav-link` typography at 12px). Space them generously on touch screens.

## Iteration Guide

1. **Reference tokens, never raw hex.** Text is `ink`, `body-muted`, `muted` or `muted-soft` on light surfaces, and `on-dark` or `on-dark-muted` on `surface-dark`. Recipe-only shades (#F5F4ED, #E8E6DC, #0F0F0E) stay inside the components that own them.
2. **Preserve the serif/sans split.** New reading text uses `body` or `body-lg`. New titles use `headline`, `title-lg` or `title-md`. Small UI uses `ui`, `label` or `caption`. Do not add new weights beyond 400, 500, 600 and 700.
3. **Keep the palette achromatic.** Adding any saturated color or any gradient breaks the system. Emphasis comes from `primary` ink fills, tonal surfaces (`surface-alt`, `surface-warm`) and weight.
4. **Make new buttons as variants of the measured set.**
   - Solid ink: `button-primary-3`.
   - Ink outline that fills on hover: `button-secondary`.
   - Soft icon button with `hairline` border: `button-secondary-3`.
   - Compact chip: `button-ghost-4`.
     Reuse their radius (`rounded.sm`, or `rounded.xs` for the chip) and their padding tokens.
5. **Respect the structural boundaries.** Spacing snaps to `base`, section rhythm is `section-padding-y`, and the container caps at `header-inner-inner-max-width`. Radius scales with object size along `rounded.xs` → `rounded.xl`, with no pills.
6. **Shadows only for floating layers.** Use the layered panel shadow for menus and popovers. In-flow cards stay tonal or hairline-ruled.
7. **Draw focus as an outline in the current text color.** Use 2px #141413 on light surfaces and 2px #FAF9F5 on dark surfaces. Never remove it, and never swap it for a glow.

## Known Gaps

- **Several recipes did not reproduce exactly.** Treat their values as close but unconfirmed:
  - `button-primary` (59% pixel match on hover)
  - `button-primary-2` (96%)
  - `card` (`card-group` height)
  - `hero` (`hero-group-4` x)
  - `header-landing` (nav-link height)
  - `nav-menu` (`nav-menu-group-2` x)
  - `nav-dropdown`, `nav-dropdown-2`, `nav-dropdown-3` (90–91% on focus)
  - the footer recipes (`footer-landing`, `footer-inner`, `footer-landing-mobile`, `footer-inner-mobile`, `footer-nav`, `footer-navigation`, `footer-link-column`, `nav-2`; heights)
  - `video` and `video-2` (46% and 54%)
  - `button-secondary-2` (icon x)
- **Uncaptured content.** The contents of the dropdown panels, footer link lists, hero title and video media were not captured. Their internal structure is inferred from screenshots only.
- **Two font-family naming schemes.** "Anthropic Serif/Sans" and "anthropicSerif/anthropicSans" appear on different pages. They are assumed to be the same families.
- **Anthropic Mono has no token.** It was measured on only one page, so its sizes and role are unverified.
- **The 96px section rhythm has no spacing token.** It appears in the page evidence and token description; only 48px is published as `section-padding-y`.
- **Weight mismatch on buttons.** The `button` token is weight 500, while the measured button labels (`button-primary-3-label`, `button-secondary-label`) render at 400.
- **Origin of `focus-ring` is unclear.** #005FCC was measured once in the recipes; every observed component focus outline uses #141413 or #FAF9F5 instead.
- **Partial state coverage.** Hover and focus were sampled only where recipes list them. Active, disabled, error and loading states, plus form validation, were not observed.
- **Unobserved behavior.** Animation, transitions, dropdown open/close motion and video playback states were not captured.
- **Limited responsive data.** Only two viewports were captured, so breakpoints and intermediate layouts are unknown.
- **Limited page coverage.** Five public pages were captured; authenticated product surfaces (Claude app, Console) are out of scope.
- **No dark theme was detected.**
