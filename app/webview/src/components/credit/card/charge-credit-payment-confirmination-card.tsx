import {
	Card,
	CardHeader,
	CardTitle,
	CardDescription,
	CardContent,
} from "@/components/ui/card";
import { Elements } from '@stripe/react-stripe-js';
import { loadStripe } from '@stripe/stripe-js';
import { ChargeCreditPaymentConfirminationForm } from '../form/charge-credit-payment-confirmination-form';


type Props = {
    clientSecret: string
}

export const ChargeCreditPaymentConfirminationCard = ({ clientSecret }: Props) => {
    // https://docs.stripe.com/payments/accept-a-payment?=&ui=elements
    
    const stripePublicKey = process.env.NEXT_PUBLIC_STRIPE_PUBLIC_KEY ?? '';
    const stripePromise = loadStripe(stripePublicKey);
    


    const options = {
        // passing the client secret obtained in step 3
        clientSecret: clientSecret,
        // Fully customizable with appearance API.
        appearance: {},
      };
    return (
        <Card className={`w-full`}>
            <CardHeader>
                <CardTitle>お支払い</CardTitle>
                <CardDescription></CardDescription>
            </CardHeader>
            <CardContent className="flex flex-col gap-3">
                <Elements stripe={stripePromise} options={options}>
                    <ChargeCreditPaymentConfirminationForm/>
                </Elements>
            </CardContent>
        </Card>
    )
}