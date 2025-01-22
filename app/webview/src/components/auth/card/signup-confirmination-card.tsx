import { cn } from "@/lib/style";
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card";
import { MailCheck } from "lucide-react";

type Props = {
    className?: string
}

export const SignupConfirminationCard = ({className}: Props) => {
	return (
		<Card className={cn("w-96 h-fit shadow-lg", className)}>
            <CardHeader className="text-center">
                <div className="mx-auto mb-4 bg-blue-50 p-3 rounded-full">
                    <MailCheck className="h-6 w-6 text-blue-500" />
                </div>
                <CardTitle className="text-xl">Verify Your Email</CardTitle>
                <CardDescription className="text-base mt-2">
                    We sent you an email with a verification link.
                </CardDescription>
            </CardHeader>
            <CardContent className="text-center space-y-3">
                <p className="text-base">
                    Check your inbox and click the verification link to activate your account. 
                </p>
                <p className="text-base">
                    Can't find the email? Check your spam folder.
                </p>
            </CardContent>
            <CardFooter className="justify-center text-sm">
                This link will expire in 30 minutes
            </CardFooter>
        </Card>
	);
};
