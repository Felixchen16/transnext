<template>
<Carousel
        v-model="value3"
        :autoplay="setting.autoplay"
        :autoplay-speed="setting.autoplaySpeed"
        :dots="setting.dots"
        :radius-dot="setting.radiusDot"
        :trigger="setting.trigger"
        :arrow="setting.arrow">
        <CarouselItem>
            <div class="demo-carousel"><img src="../../../static/images/hero/hero-image-3.jpg" alt="hero image"></div>
        </CarouselItem>
        <CarouselItem>
            <div class="demo-carousel"><img src="../../../static/images/hero/hero-image-4.jpg" alt="hero image"></div>
        </CarouselItem>
        <CarouselItem>
            <div class="demo-carousel"><img src="../../../static/images/hero/hero-image-3.jpg" alt="hero image"></div>
        </CarouselItem>
        <CarouselItem>
            <div class="demo-carousel"><img src="../../../static/images/hero/hero-image-4.jpg" alt="hero image"></div>
        </CarouselItem>
    </Carousel>
</template>

<script>
    export default {
        data () {
            return {
                value3: 0,
                setting: {
                    autoplay: true,
                    autoplaySpeed: 5000,
                    dots: 'inside',
                    radiusDot: true,
                    trigger: 'click',
                    arrow: 'hover'
                }
            }
        },
    }
</script>

<style scoped>
</style>
