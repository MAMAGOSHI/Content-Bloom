// ==========================================
// GET PAGE ELEMENTS
// ==========================================

const modeCards =
    document.querySelectorAll(".mode-card");


const textStudio =
    document.getElementById("textStudio");


const imageStudio =
    document.getElementById("imageStudio");



// ==========================================
// MODE SWITCHING
// ==========================================

modeCards.forEach(function(card) {

    card.addEventListener("click", function() {


        // Coming soon features

        if (
            card.classList.contains("coming-soon")
        ) {

            alert(
                "🌸 This Content Bloom feature is coming soon!"
            );

            return;

        }


        // Remove active state

        modeCards.forEach(function(item) {

            item.classList.remove("active");

        });


        // Activate selected card

        card.classList.add("active");


        const mode =
            card.dataset.mode;



        // TEXT

        if (mode === "text") {

            textStudio.classList.remove(
                "hidden"
            );

            imageStudio.classList.add(
                "hidden"
            );


            textStudio.scrollIntoView({
                behavior: "smooth"
            });

        }



        // IMAGE

        if (mode === "image") {

            textStudio.classList.add(
                "hidden"
            );

            imageStudio.classList.remove(
                "hidden"
            );


            imageStudio.scrollIntoView({
                behavior: "smooth"
            });

        }

    });

});



// ==========================================
// TEXT STUDIO
// ==========================================

const generateButton =
    document.getElementById(
        "generateButton"
    );


const loading =
    document.getElementById(
        "loading"
    );


const resultSection =
    document.getElementById(
        "result-section"
    );


const result =
    document.getElementById(
        "result"
    );


const copyButton =
    document.getElementById(
        "copyButton"
    );



generateButton.addEventListener(
    "click",
    async function() {


        const topic =
            document.getElementById(
                "topic"
            ).value;


        const contentType =
            document.getElementById(
                "contentType"
            ).value;


        const platform =
            document.getElementById(
                "platform"
            ).value;


        const audience =
            document.getElementById(
                "audience"
            ).value;


        const tone =
            document.getElementById(
                "tone"
            ).value;


        const goal =
            document.getElementById(
                "goal"
            ).value;


        const length =
            document.getElementById(
                "length"
            ).value;



        if (!topic.trim()) {

            alert(
                "🌱 Tell Content Bloom your idea first."
            );

            return;

        }



        generateButton.disabled = true;


        generateButton.textContent =
            "🌸 Growing your content...";


        loading.classList.remove(
            "hidden"
        );


        resultSection.classList.add(
            "hidden"
        );



        try {


            const response =
                await fetch(
                    "/generate",
                    {

                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            content_type:
                                contentType,

                            topic:
                                topic,

                            platform:
                                platform,

                            audience:
                                audience,

                            tone:
                                tone,

                            goal:
                                goal,

                            length:
                                length

                        })

                    }
                );



            const data =
                await response.json();



            if (!response.ok) {

                throw new Error(
                    data.error ||
                    "Something went wrong."
                );

            }



            result.textContent =
                data.content;


            resultSection.classList.remove(
                "hidden"
            );


        }


        catch (error) {

            alert(
                error.message
            );

        }


        finally {

            generateButton.disabled =
                false;


            generateButton.textContent =
                "✨ Bloom my content";


            loading.classList.add(
                "hidden"
            );

        }

    }
);



// ==========================================
// COPY TEXT
// ==========================================

copyButton.addEventListener(
    "click",
    async function() {

        await navigator.clipboard.writeText(
            result.textContent
        );


        copyButton.textContent =
            "Copied!";


        setTimeout(
            function() {

                copyButton.textContent =
                    "Copy";

            },
            2000
        );

    }
);



// ==========================================
// IMAGE STUDIO
// ==========================================

const generateImageButton =
    document.getElementById(
        "generateImageButton"
    );


const imagePromptResult =
    document.getElementById(
        "imagePromptResult"
    );


const imagePrompt =
    document.getElementById(
        "imagePrompt"
    );


const copyImagePrompt =
    document.getElementById(
        "copyImagePrompt"
    );



generateImageButton.addEventListener(
    "click",
    async function() {


        const idea =
            document.getElementById(
                "imageIdea"
            ).value;


        const style =
            document.getElementById(
                "imageStyle"
            ).value;


        const mood =
            document.getElementById(
                "imageMood"
            ).value;


        const audience =
            document.getElementById(
                "imageAudience"
            ).value;


        const platform =
            document.getElementById(
                "imagePlatform"
            ).value;



        if (!idea.trim()) {

            alert(
                "🌱 Tell Content Bloom what you want to create."
            );

            return;

        }



        generateImageButton.disabled =
            true;


        generateImageButton.textContent =
            "🌸 Creating your visual...";



        try {


            const response =
                await fetch(
                    "/generate-image-prompt",
                    {

                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            idea:
                                idea,

                            style:
                                style,

                            mood:
                                mood,

                            audience:
                                audience,

                            platform:
                                platform

                        })

                    }
                );



            const data =
                await response.json();



            if (!response.ok) {

                throw new Error(
                    data.error ||
                    "Something went wrong."
                );

            }



            imagePrompt.textContent =
                data.prompt;


            imagePromptResult.classList.remove(
                "hidden"
            );

        }


        catch (error) {

            alert(
                error.message
            );

        }


        finally {

            generateImageButton.disabled =
                false;


            generateImageButton.textContent =
                "🖼️ Create my visual";

        }

    }
);



// ==========================================
// COPY IMAGE PROMPT
// ==========================================

copyImagePrompt.addEventListener(
    "click",
    async function() {


        await navigator.clipboard.writeText(
            imagePrompt.textContent
        );


        copyImagePrompt.textContent =
            "Copied!";


        setTimeout(
            function() {

                copyImagePrompt.textContent =
                    "Copy";

            },
            2000
        );

    }
);