$(document).ready(function () {

    $(document).on('click', '#thumbnailML', function () {

        $('#boxThumbnailML').attr('src', $(this).data('img'));

    });
});



var client = algoliasearch(appConfig.algolia_app, appConfig.algolia_key);
var index = client.initIndex('product_index');

index.search('product_index', searchCallback);

index.search(
    'product_index', {
        hitsPerPage: 5,
        facets: '*',
        maxValuesPerFacet: 10
    },
    searchCallback
);

function searchCallback(err, content) {
    if (err) {
        console.error(err);
        return;
    }

    console.log(content);
}