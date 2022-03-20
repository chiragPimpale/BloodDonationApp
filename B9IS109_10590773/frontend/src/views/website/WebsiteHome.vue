<!--
Home component inhertited from WebsiteLyout
-->
<template>
<div>
    <img src="https://i1.wp.com/www.pacificprime.co.th/blog/wp-content/uploads/2020/06/banner-1138x493-v2.jpg?fit=1138%2C493&ssl=1" alt="" style="width:100%" />

    <div class="blood-gallery mt-5">
        <div class="container">
            <h1 class="text-danger text-center mb-4">Gallery</h1>
        </div>
        <div class="container d-flex flex-wrap">
            <div class="card" style="width: 20rem;margin-right:50px;margin-bottom:50px">
                <img style="width:100%;height:220px" src="https://thumbs.dreamstime.com/b/young-man-making-blood-donation-hospital-focus-hand-young-man-making-blood-donation-hospital-166498077.jpg" class="card-img-top" alt="...">
                <div class="card-body">
                    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                </div>
            </div>
            <div class="card" style="width: 20rem;margin-right:50px;margin-bottom:50px">
                <img style="width:100%;height:220px" src="https://media.istockphoto.com/photos/world-hemophilia-day-concept-with-red-blood-drop-simbol-and-hands-on-picture-id1306204732?b=1&k=20&m=1306204732&s=170667a&w=0&h=VtqvHGpxxWrejTYTkOsR-Y4Oo-a0wfIdGP02ECVvU-U=" class="card-img-top" alt="...">
                <div class="card-body">
                    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                </div>
            </div>
            <div class="card" style="width: 20rem;margin-right:50px;margin-bottom:50px">
                <img style="width:100%;height:220px" src="https://media.istockphoto.com/vectors/blood-donation-concept-vector-id1256555401?k=20&m=1256555401&s=612x612&w=0&h=We4Ckw72r8-RSK_TOVG2jWtui1ntlQNgYeDo1lLi1qg=" class="card-img-top" alt="...">
                <div class="card-body">
                    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                </div>
            </div>
            <div class="card" style="width: 20rem;margin-right:50px;margin-bottom:50px">
                <img style="width:100%;height:220px" src="https://image.shutterstock.com/image-vector/world-blood-donor-day-poster-260nw-1755335978.jpg" class="card-img-top" alt="...">
                <div class="card-body">
                    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                </div>
            </div>
            <div class="card" style="width: 20rem;margin-right:50px;margin-bottom:50px">
                <img style="width:100%;height:220px" src="https://png.pngtree.com/png-clipart/20200701/original/pngtree-public-welfare-blood-donation-png-image_5398288.jpg" class="card-img-top" alt="...">
                <div class="card-body">
                    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                </div>
            </div>
            <div class="card" style="width: 20rem;margin-right:50px;margin-bottom:50px">
                <img style="width:100%;height:220px" src="https://img.freepik.com/free-vector/hands-saving-blood-drop_1017-19141.jpg?size=338&ext=jpg&ga=GA1.2.1480491136.1638748800" class="card-img-top" alt="...">
                <div class="card-body">
                    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: "WebsiteHome",
    // request to change title of web page
    mounted() {
        document.title = "Website | Home"
    }
}
</script>
