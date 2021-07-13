exports.handler = async function(event, context) {
    console.log(event)
    console.log(context)

    return {
        statusCode: 200,
        body: JSON.stringify({message: "Thanks"})
    };
}
