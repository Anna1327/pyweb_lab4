<script>

    import { onMount, onDestroy } from 'svelte';
    import Cookies from 'js-cookie/src/js.cookie.js'
    
   let food = [
		{ title:       'Bell Pepper',
          img:         'images/product-1.jpg', 
          description: 'Far far away, behind the word mountains, far from the countries',
          currency:    '$',
          price:       80.00,
          quantity:     1,
          total_price: 80.00
          },
        { title:       'Stawberry',
          img:         'images/product-2.jpg', 
          description: 'Far far away, behind the word mountains, far from the countries',
          currency:    '$',
          price:       120.00,
          quantity:     1,
          total_price: 120.00
          },
        { title:       'Green beans',
          img:         'images/product-3.jpg', 
          description: 'Far far away, behind the word mountains, far from the countries',
          currency:    '$',
          price:       20.00,
          quantity:     1,
          total_price: 20.00
          },          
	];
    
    function onInterval(callback, ms) {
        const interval = setInterval(callback, ms);
        
        onDestroy(() => {
            clearInterval(interval);
        });    
    }
    
    function getRef(id) {return document.getElementById(id).href;};    

    
    const IMG_GEN_URL = getRef('picsum-ref');
   
    var count = 0;
    onInterval(async () => {
        console.log(IMG_GEN_URL);
        const response = await fetch(IMG_GEN_URL);
        food[count].img = await response.url;  
        count += 1;
        if (count >= food.length)
            count = 0;    
    }, 10000);
    
    
    const CSRF_TOKEN = Cookies.get('csrftoken');
    const WISHLIST_URL = getRef("wishlist-ref");
    
    onInterval(async () => {
        const response = await fetch(WISHLIST_URL, {
                                             headers: {
                                                'Content-Type': 'application/json',
                                                'Accept': 'application/json, text-plain, */*',
                                                'X-Requested-With': 'XMLHttpRequest',
                                                'X-CSRFToken': CSRF_TOKEN
                                             },
                                             method: 'POST',
                                             credentials: 'same-origin',
                                             body: JSON.stringify({})
                                     });
        console.log(await response.text());    
    
        }, 1000);
    
    

    
    

   
    //onMount(async () => {
    //    const response = await fetch(IMG_GEN_URL);
    //    food[0].img = await response.url;    
   // });


	    
</script>

<main>
    
<table class="table">
    <thead class="thead-primary">
      <tr class="text-center">
        <th>&nbsp;</th>
        <th>Product List</th>
        <th>&nbsp;</th>
        <th>Price</th>
        <th>Quantity</th>
        <th>Total</th>
      </tr>
    </thead>
    <tbody >
    
        {#each food as item }
          <tr class="text-center">
            <td class="product-remove"><a href="."><span class="ion-ios-close"></span></a></td>						        
            <td class="image-prod"><div class="img" style="background-image:url({item.img});"></div></td>						        
            <td class="product-name">
                <h3>{item.title}</h3>
                <p>{item.description}</p>
            </td>						        
            <td class="price">{item.currency}{item.price}</td>						        
            <td class="quantity">
                <div class="input-group mb-3">
                <input type="number" name="quantity" class="quantity form-control input-number" bind:value={item.quantity} min=1 max=100>
            </div>
          </td>						        
            <td class="total">{item.currency}{item.quantity*item.price}</td>
          </tr><!-- END TR-->
        {/each}

    </tbody>
  </table>


</main>

<style>

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>